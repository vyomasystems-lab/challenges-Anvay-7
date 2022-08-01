## Verification Environment
The test drives inputs to the Design Under Test (mux module here) which takes in  31 2-bit inputs *(inp0-inp30)*, a 5-bit select line *(sel)* and gives out a 2-bit output *(out)*
The values are assigned to the input port using

    for i in range(31):
	    value = random.randint(0,3)
	    inputs[i] = value
	    code_line =  f"dut.inp{i}.value = {value}"
	    exec(code_line)

The assert statement in a try - except block is used to collect all the bugs (and not stop the test after a bug is found)

    try:
	    assert dut.out.value == inputs[sel_value]
    except  AssertionError  as e:
    	fail_count+=1
	    fail_msg='\33[31m'+f"Test failed with sel = {sel_value}"+'\x1b[0m'
	    failed_cases.append(fail_msg)
	    print("\t",fail_msg)

The following error is seen:
<img src="./images/mux_error.PNG" alt="Mux error" />