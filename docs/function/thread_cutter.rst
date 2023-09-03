.. _thread_cutter:

=============
Thread cutter
=============

**Thread cutting procedure**

Thread cutting singnal is switched on when the angle value **D03** has been reached, the switched off when the angle value **D04**. If the position is not reached because of a mechanical error, the thread cutter signal is switched off after 500ms for protect the magnet from damage.


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
| A06 | 1 | 0 | - | Thread cutter:<br>0 = Off;<br>1 = On |
| S07 | 300 | 150 | spm | Thread cutter speed |
| D03 | 359 | 0 | 1° | Thread cutter power on angle |
| D04 | 359 | 0 | 1° | Thread cutter power off angle |
| O38 | 1 | 0 | - | Pedal must be reset before restart sewing after thread cutting procedure<br>0 = Off;<br>1 = On |

**Short thread cutter**

| No. | Max | Min | Unit | Description |
| --- | --- | --- | --- | --- |
| A42 | 1 | 0 | - | Short thread cutter:<br> 0 = Off;<br> 1 = On |
| D19 | 359 | 0 | 1° | Reverse of short thread trimming power on angle |
| D20 | 359 | 0 | 1° | Reverse of short thread trimming power off angle |
| D21 | 359 | 0 | 1° | Zero stitch length of short thread trimming power on angle |
| D22 | 359 | 0 | 1° | Zero stitch length of short thread trimming power off angle |
