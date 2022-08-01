# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge


seq_states={"000":"IDLE","001":"SEQ_1","010":"SEQ_10","011":"SEQ_101","100":"SEQ_1011"}

def get_state(pattern):
    """Get the expected state value"""
    if pattern[-4:]=="1011":
        state="SEQ_1011"
    elif pattern[-3:] == "101":
        state="SEQ_101"
    elif pattern[-2:]=="10":
        state="SEQ_10"
    elif pattern[-1:]=="1":
        state="SEQ_1"
    else:
        state="IDLE"
    return state

@cocotb.test()
async def custom_input1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    input_pattern="1010111011"
    temp_seq=""
    seq="1011"
    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    # dut.inp_bit.value = 0 
    await FallingEdge(dut.clk)
    dut._log.info(f'Input bit = {dut.inp_bit.value} | DUT = {dut.seq_seen.value} | Current State = {dut.current_state.value} ({seq_states[str(dut.current_state.value)]})')
    # cocotb.log.info('#### CTB: Develop your test here! ######')
    for bit in input_pattern:
        temp_seq+=bit
        expected_state = get_state(temp_seq)
        dut.inp_bit.value = int(bit)
        await FallingEdge(dut.clk)
        if temp_seq.find(seq)>-1:
            output=1
            temp_seq=""
        else:
            output=0

        # print(dut.current_state.value)
        current_state=str(dut.current_state.value)
        dut._log.info(f'Input bit = {dut.inp_bit.value} | DUT = {dut.seq_seen.value} | Current State = {current_state} ({seq_states[current_state]})')

        assert (output==int(dut.seq_seen.value)) & (expected_state==seq_states[current_state]) ,'\33[31m'+f"Input bit = {dut.inp_bit.value}, Expected DUT output = {output}, DUT value = {dut.seq_seen.value} | Expected DUT state = {expected_state}  DUT state = {seq_states[current_state]}"+'\x1b[0m'


@cocotb.test()
async def custom_input2(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    input_pattern="10101010"
    temp_seq=""
    seq="1011"
    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    # dut.inp_bit.value = 0 
    await FallingEdge(dut.clk)
    dut._log.info(f'Input bit = {dut.inp_bit.value} | DUT = {dut.seq_seen.value} | Current State = {dut.current_state.value} ({seq_states[str(dut.current_state.value)]})')
    # cocotb.log.info('#### CTB: Develop your test here! ######')
    for bit in input_pattern:
        temp_seq+=bit
        expected_state = get_state(temp_seq)
        dut.inp_bit.value = int(bit)
        await FallingEdge(dut.clk)
        if temp_seq.find(seq)>-1:
            output=1
            temp_seq=""
        else:
            output=0

        # print(dut.current_state.value)
        current_state=str(dut.current_state.value)
        dut._log.info(f'Input bit = {dut.inp_bit.value} | DUT = {dut.seq_seen.value} | Current State = {current_state} ({seq_states[current_state]})')

        assert (output==int(dut.seq_seen.value)) & (expected_state==seq_states[current_state]) ,'\33[31m'+f"Input bit = {dut.inp_bit.value}, Expected DUT output = {output}, DUT value = {dut.seq_seen.value} | Expected DUT state = {expected_state}  DUT state = {seq_states[current_state]}"+'\x1b[0m'



@cocotb.test()
async def random_input(dut):
    """Randomised input pattern """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    random_no=random.randint(0,2**16)
    input_pattern =bin(random_no).replace("0b", "")
    print("Random input pattern is = ", input_pattern, " In decimal form = ", random_no)
    temp_seq=""
    seq="1011"
    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    # dut.inp_bit.value = 0 
    await FallingEdge(dut.clk)
    dut._log.info(f'Input bit = {dut.inp_bit.value} | DUT = {dut.seq_seen.value} | Current State = {dut.current_state.value} ({seq_states[str(dut.current_state.value)]})')
    # cocotb.log.info('#### CTB: Develop your test here! ######')
    for bit in input_pattern:
        temp_seq+=bit
        expected_state = get_state(temp_seq)
        dut.inp_bit.value = int(bit)
        await FallingEdge(dut.clk)
        if temp_seq.find(seq)>-1:
            output=1
            temp_seq=""
        else:
            output=0

        # print(dut.current_state.value)
        current_state=str(dut.current_state.value)
        dut._log.info(f'Input bit = {dut.inp_bit.value} | DUT = {dut.seq_seen.value} | Current State = {current_state} ({seq_states[current_state]})')

        assert (output==int(dut.seq_seen.value)) & (expected_state==seq_states[current_state]) ,'\33[31m'+f"Input bit = {dut.inp_bit.value}, Expected DUT output = {output}, DUT value = {dut.seq_seen.value} | Expected DUT state = {expected_state}  DUT state = {seq_states[current_state]}"+'\x1b[0m'