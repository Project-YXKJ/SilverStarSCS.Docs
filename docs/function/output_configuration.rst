.. _output_configuration:

# Output configuration

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
     
| No. | Max | Min | Unit | Description |
| --- | --- | --- | --- | --- |
| A71 | 13 | 0 | - | Function output-01:<br>0 = No function;<br>1 = Thread cutter;<br>2 = Thread tension;<br>3 = Thread clamp;<br>4 = Reverse;<br>5 = Sewing foot lifter;<br>6 = Stroke;<br>7 = Additional thread tension;<br>8 = Thread wiper;<br>9 = Second stitch length;<br/>10 = Needle cooling;<br>11 = Additional cutter for short thread cutter machine;<br>12 = Seam center guide;<br>13 = Zero stitch length for short thread cutter machine;<br>14 = Auto corner for 2-needle machine;<br>15 = Puller |
| A72 | 13 | 0 | - | Function of output-02, refer to A71 |
| A73 | 13 | 0 | - | Function of output-03, refer to A71 |
| A74 | 13 | 0 | - | Function of output-04, refer to A71 |
| A75 | 13 | 0 | - | Function of output-05, refer to A71 |
| A76 | 13 | 0 | - | Function of output-06, refer to A71 |
| A77 | 13 | 0 | - | Function of output-07, refer to A71 |
| A78 | 13 | 0 | - | Function of output-08, refer to A71 |
| A79 | 13 | 0 | - | Function of output-09, refer to A71 |
| A80 | 13 | 0 | - | Function of output-10, refer to A71 |

**How to setup the function of output ports**:

follow the steps:

- Confirm which output port is connected to the solenoid valve, like output-07 or output-06. In this step, you need to know the specific model of the system you are using, then refer to its wiring diagram.
- Refer to the table at the beginning of this chapter, get the parameter value you need.
- Restart the system

Let's take an example:

For example, if **Output-01** is connected, set the function of **Output-01** to puller, that is, **A71** is set to 15 (15 is the code for puller function).
