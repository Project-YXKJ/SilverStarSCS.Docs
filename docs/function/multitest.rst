# Multitest

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
| O23 | 60 | 1 | s | Running time of an endurance cycle |
| O24 | 60 | 1 | s | Standby time of an endurance cycle |
| O25 | 720 | 1 | h | Total endurance time |
| O26 | 1 | 0 | - | Endurance running function<br>0 = Off<br>1 = On |

When the endurance test starts, the machine will run automatically until the test time which set by **O25** is reached.
