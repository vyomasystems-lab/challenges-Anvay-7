# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

class TestFail(Exception):
    """Custom Error"""

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    inputs={}
    fail_count=0
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

        #assert dut.out.value == inputs[sel_value], f"Test failed with sel = {sel_value}"
        try: 
            assert dut.out.value == inputs[sel_value]
        except AssertionError as e:
            fail_count+=1
            print(f"\tTest failed with sel = {sel_value}")

    if fail_count>0:
        raise TestFail(f"Test cases failed {fail_count} times! :(")



 # dut.inp0.value = random.randint(0,3)
    # dut.inp1.value = random.randint(0,3)
    # dut.inp2.value = random.randint(0,3)
    # dut.inp3.value = random.randint(0,3)
    # dut.inp4.value = random.randint(0,3)
    # dut.inp5.value = random.randint(0,3)
    # dut.inp6.value = random.randint(0,3)
    # dut.inp7.value = random.randint(0,3)
    # dut.inp8.value = random.randint(0,3)
    # dut.inp9.value = random.randint(0,3)
    # dut.inp10.value = random.randint(0,3)
    # dut.inp11.value = random.randint(0,3)
    # dut.inp12.value = random.randint(0,3)
    # dut.inp13.value = random.randint(0,3)
    # dut.inp14.value = random.randint(0,3)
    # dut.inp15.value = random.randint(0,3)
    # dut.inp16.value = random.randint(0,3)
    # dut.inp17.value = random.randint(0,3)
    # dut.inp18.value = random.randint(0,3)
    # dut.inp19.value = random.randint(0,3)
    # dut.inp20.value = random.randint(0,3)
    # dut.inp21.value = random.randint(0,3)
    # dut.inp22.value = random.randint(0,3)
    # dut.inp23.value = random.randint(0,3)
    # dut.inp24.value = random.randint(0,3)
    # dut.inp25.value = random.randint(0,3)
    # dut.inp26.value = random.randint(0,3)
    # dut.inp27.value = random.randint(0,3)
    # dut.inp28.value = random.randint(0,3)
    # dut.inp29.value = random.randint(0,3)
    # dut.inp30.value = random.randint(0,3)
    # dut.inp31.value = random.randint(0,3)