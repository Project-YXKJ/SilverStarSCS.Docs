# Service counter

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
| A60 | 1 | 0 | - | Service counter:<br>0 = Off;<br>1 = On |
| A61 | 9999 | 1 | - | Reset value of service counter |
| A62 | 200 | 1 | stitches | Factor of service counter |
| A63 | 9999 | 0 | - | Counter value |

Using service counter allows users to remind regular mechanical maintenance.

**Here is a formula**:

Remaining amount = reset value of the bobbin thread counter(A61) – bobbin thread counter value(A63).

**Setup steps**:

- Set an appropriate value for **A62**, every time N stitches are sewn which set by parameter **A63**, the counter(O44) increases by 1.
- Set an appropriate value for **A61**, this is a very variable value, which depends on how often you want to maintain.
- Enable counter.
- As the sewing, the remaining thread amount(A61-A63) is counted down, when it reaches 0, the machine will stop, and the controller will throw a warning(Code 7). A reset is needed if you want continue.
