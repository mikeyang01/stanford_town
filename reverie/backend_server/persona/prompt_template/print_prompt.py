"""
Author: Joon Sung Park (joonspk@stanford.edu)

File: print_prompt.py
Description: For printing prompts when the setting for verbose is set to True.
"""
import sys
sys.path.append('../')

import json
import numpy
import datetime
import random

from global_methods import *
from persona.prompt_template.gpt_structure import *
from utils import *

##############################################################################
#                    PERSONA Chapter 1: Prompt Structures                    #
##############################################################################

def print_run_prompts(prompt_template=None, 
                      persona=None, 
                      gpt_param=None, 
                      prompt_input=None,
                      prompt=None, 
                      output=None): 
  print (f"====>{prompt_template}==========================")
  print ("---->persona---------------------------------------------------")
  print (persona.name)
  print ("---->gpt_param-------------------------------------------------")
  print (gpt_param)
  #print ("---->prompt_input---------------------------------------------")
  #print (prompt_input)
  #print ("---->prompt_without_temp--------------------------------------")
  #print (prompt)
  print ("---->Formatted output------------------------------------------")
  print (output) 
  print ("====END=======================================================")
  print ("\n")
