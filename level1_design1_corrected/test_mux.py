# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

class TestFail(Exception):
    """Custom Error"""

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    # cocotb.log.info('##### CTB: Develop your test here ########')
    
    inputs={}
    fail_count=0
    failed_cases=[]
    for i in range(31):
        value = random.randint(0,3)
        inputs[i] = value
        code_line = f"dut.inp{i}.value = {value}"
        exec(code_line)

    print("The inputs to the mux are: ", inputs)
    for sel_value in range(31):
        dut.sel.value = sel_value

        await Timer(2,units='ns')

        dut._log.info(f'sel = {sel_value:05} DUT = {int(dut.out.value):02}')
        try: 
            assert dut.out.value == inputs[sel_value]
        except AssertionError as e:
            fail_count+=1
            fail_msg='\33[31m'+f"Test failed with sel = {sel_value}"+'\x1b[0m'
            failed_cases.append(fail_msg)
            print("\t",fail_msg)

    if fail_count>0:
        print('\x1b[0;37;45m',"The failed cases are: ",'\x1b[0m')
        for case in failed_cases:
            print(case)
        raise TestFail('\x1b[0;30;41m'+f"Test cases failed {fail_count} times! :("+'\x1b[0m')
    else:
        print('\x1b[0;30;42m'+"No test cases failed! :)"+'\x1b[0m')
