# Needle cooling

Parameter List
==============

P00
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description
     | The description can also start on the next line.
     | value1: text;
     | value2: text.
     
| No. | Max | Min | Unit | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| --- | --- | --- | --- | --- |
| A48 | 1 | 0 | - | Needle cooling function:<br>0 = Off;<br>1 = On |
| O93 | 999 | 1 | ms | Full activation duration |
| O94 | 100 | 1 | % | Duty cycle in time period when PWM activation |
| S18 | 100 | 4500 | S/min | Needle cooling start speed |
| T16 | 10 | 0 | s | Needle cooling follow up time |

When the machine is running, the needle cooling is to be activated.

**How it works**:

Above the speed set by **S18**, the needle cooling start;

Below the speed set by **S18**, the needle cooling does not stop immediately, needle cooling to continue until the set time(**T16**) has elapsed.

During the follow-up time, if the speed exceeds **S18** again, the needle cooling start again.
