import cocotb
from cocotb.triggers import Timer
import random
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge
from copy import deepcopy
from collections import deque
req_lst=["0000","0001","0001","1001","1101","0001","0000"]

device_lut={None:"0000",0:"0001",1:"0010",2:"0100",3:"1000"}

def get_grant(req,old_grant,dev):
    temp_dev=deepcopy(dev)
    flag=True
    i=0
    # old_grant=grant
    while(i<4 and flag==True):
        if (req[3-temp_dev[-1]]=="1"):
            grant=temp_dev[-1]
            flag=False
        else:
            temp_dev.rotate(1)
            grant=None
        i+=1
    if grant is not None and old_grant!=device_lut[grant]:
        dev.rotate(1)
    else:
        grant=None
    return device_lut[grant]


@cocotb.test()
async def repeat_grant_bug(dut):
    clock = Clock(dut.clk, 10, units="us")  
    cocotb.start_soon(clock.start()) 

    dut.rst_an.value=1
    await Timer(2,units='us')
    dut.rst_an.value=0
    await Timer(2,units='us')
    expected_grant=None
    dev=deque([3,2,1,0])

    for req in req_lst:
        dut.rst_an.value=1
        dut.req.value=int(req,2)
        await FallingEdge(dut.clk)
        expected_grant=get_grant(req,expected_grant,dev)
        # print(dut.grant.value,'  ',expected_grant)
        dut._log.info(f'Request = {req}, DUT output = {dut.grant.value}, Expected output = {expected_grant}')

        assert str(dut.grant.value) == expected_grant, '\33[31m'+f"DUT output: {dut.grant.value} != Expected output: {expected_grant} for request = {req}"+'\x1b[0m'