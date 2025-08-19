Warnings, error and information messages
========================================

The exception messages of *SilverStar Sewing Control System* is divided into three
groups, as shown in the following table:

=========== ==== ===================================================================
Level       Code Description
=========== ==== ===================================================================
Error       Err  Switch off the control and eliminate the problem
Warning     Wrn  Eliminate the state that caused to the warning, the control will
                 normally worked
Information Inf  Work can be continued, only exception message needs to be confirmed
=========== ==== ===================================================================

Exception quick reference
-------------------------

Error messages
~~~~~~~~~~~~~~

================= ============================ =============================
Code              Messages                     Remedial action
================= ============================ =============================
:exc:`ExcCode101` ac power excess voltage      :meth:`ExcCode101.solution()`
:exc:`ExcCode103` bus excess voltage           :meth:`ExcCode103.solution()`
:exc:`ExcCode106` motor excess current         :meth:`ExcCode106.solution()`
:exc:`ExcCode107` overload/motor speed too low :meth:`ExcCode107.solution()`
:exc:`ExcCode108` motor excess phase current   :meth:`ExcCode108.solution()`
:exc:`ExcCode109` motor blocked when start     :meth:`ExcCode109.solution()`
:exc:`ExcCode110` motor blocked                :meth:`ExcCode110.solution()`
:exc:`ExcCode111` motor uvw signal             :meth:`ExcCode111.solution()`
:exc:`ExcCode112` motor encoder error          :meth:`ExcCode112.solution()`
:exc:`ExcCode113` magnet/solenoid over-current :meth:`ExcCode113.solution()`
:exc:`ExcCode114` motor encoder error          :meth:`ExcCode114.solution()`
:exc:`ExcCode126` panel connection error       :meth:`ExcCode126.solution()`
:exc:`ExcCode127` panel connection lost        :meth:`ExcCode127.solution()`
:exc:`ExcCode128` data checksum error          :meth:`ExcCode128.solution()`
:exc:`ExcCode129` stepper connection error     :meth:`ExcCode129.solution()`
:exc:`ExcCode130` data checksum error          :meth:`ExcCode130.solution()`
:exc:`ExcCode191` Controller: upgrade          :meth:`ExcCode191.solution()`
:exc:`ExcCode192` Controller: upgrade          :meth:`ExcCode192.solution()`
:exc:`ExcCode193` Controller: upgrade          :meth:`ExcCode193.solution()`
:exc:`ExcCode194` Controller: upgrade          :meth:`ExcCode194.solution()`
:exc:`ExcCode195` Controller: upgrade          :meth:`ExcCode195.solution()`
:exc:`ExcCode196` Controller: upgrade          :meth:`ExcCode196.solution()`
:exc:`ExcCode197` Controller: upgrade          :meth:`ExcCode197.solution()`
:exc:`ExcCode198` Controller: upgrade          :meth:`ExcCode198.solution()`
:exc:`ExcCode199` Controller: upgrade          :meth:`ExcCode199.solution()`
:exc:`ExcCode181` HMI: upgrade                 :meth:`ExcCode181.solution()`
:exc:`ExcCode182` HMI: upgrade                 :meth:`ExcCode182.solution()`
:exc:`ExcCode183` HMI: upgrade                 :meth:`ExcCode183.solution()`
:exc:`ExcCode184` HMI: upgrade                 :meth:`ExcCode184.solution()`
:exc:`ExcCode185` HMI: upgrade                 :meth:`ExcCode185.solution()`
:exc:`ExcCode186` HMI: upgrade                 :meth:`ExcCode186.solution()`
:exc:`ExcCode187` HMI: upgrade                 :meth:`ExcCode187.solution()`
:exc:`ExcCode188` HMI: upgrade                 :meth:`ExcCode188.solution()`
:exc:`ExcCode189` HMI: upgrade                 :meth:`ExcCode189.solution()`
================= ============================ =============================

Warning messages
~~~~~~~~~~~~~~~~

The code of the warning message is always less than 100.

=============== ====================== ===========================
Code            Messages               Remedial action
=============== ====================== ===========================
:exc:`ExcCode1` pedal                  :meth:`ExcCode1.solution()`
:exc:`ExcCode2` tilt switch            :meth:`ExcCode2.solution()`
:exc:`ExcCode3` shortkeys              :meth:`ExcCode3.solution()`
:exc:`ExcCode4` shortkeys              :meth:`ExcCode4.solution()`
:exc:`ExcCode5` bobbin counter/monitor :meth:`ExcCode5.solution()`
:exc:`ExcCode6` upper thread breaking  :meth:`ExcCode6.solution()`
:exc:`ExcCode7` service counter        :meth:`ExcCode7.solution()`
:exc:`ExcCode8` eye protection         :meth:`ExcCode8.solution()`
:exc:`ExcCode9` slide monitoring       :meth:`ExcCode9.solution()`
=============== ====================== ===========================

Information messages
~~~~~~~~~~~~~~~~~~~~

The code of the information message is always less than 100.

================ ========= ============================
Code             Messages  Remedial action
================ ========= ============================
:exc:`ExcCode50` oil level :meth:`ExcCode50.solution()`
================ ========= ============================

Error message list
------------------

.. exception:: ExcCode101

    AC power supply voltage is too high

    .. method:: solution()

       Check the ac voltage;
       Replace the controller.

.. exception:: ExcCode103

    Bus voltage is too high

    .. method:: solution()

       Check the brake circuit, replace the brake resistor;
       Replace the controller.

.. exception:: ExcCode106

    The bus current is too high

    .. method:: solution()

       Check the motor encoder connection;
       Check if the right :term:`MACHINE ID` is seted;
       Replace the controller;

.. exception:: ExcCode107

    Overload, the speed of main motor is too low

    .. method:: solution()

       The shaft is blocked;
       The material is too thick.

.. exception:: ExcCode108

    Overload, the current command of main motor exceeds the maximum value

    .. method:: solution()

       The shaft is blocked;
       The material is too thick.

.. exception:: ExcCode109

    The main motor starts failed

    .. method:: solution()

       Restart the machine from where the sewing material is thinner;
       The shaft is blocked;
       The material is too thick.

.. exception:: ExcCode110

    The synchronizer signal is not detected

    .. method:: solution()

       Check the synchronizaer signal;
       The shaft is blocked;
       The material is too thick.

.. exception:: ExcCode111

    Motor UVW signal is abnormal

    .. method:: solution()

       Check the UVW signal;
       Replace motor encoder

.. exception:: ExcCode112

    The motor synchronization signal cannot be detected for a long time after
    press the pedal.

    .. method:: solution()

       Check the synchronizaer signal;
       Replace motor encoder.

.. exception:: ExcCode113

    The solenoid current is too high

    .. method:: solution()

       Check the solenoid;
       Replace the controller or solenoid;

.. exception:: ExcCode114

    Abnormal value of motor angle

    .. method:: solution()

       Check the motor encoder connection;
       Check the hall sensor;

.. exception:: ExcCode126

    The paramter synchronization is failed

    .. method:: solution()

       Check the panel connection;
       Restart the control box

.. exception:: ExcCode127

    The panel is reconnected when some special mode

    .. method:: solution()

       Restart the controlbox

.. exception:: ExcCode128

    Parameters verified failed

    .. method:: solution()

       Restart the controlbox;
       Update software.

.. exception:: ExcCode129

    The step drive communication failed

    .. method:: solution()

       Restart the controlbox;
       Check the communication cable.

.. exception:: ExcCode130

    Parameters version verified failed

    .. method:: solution()

       Update the software of controlbox or panel.

.. exception:: ExcCode191

    Controller upgrade files data error: wrong file

    .. method:: solution()

       Update software

.. exception:: ExcCode192

    Controller upgrade files data error: wrong page

    .. method:: solution()

       Copy the upgrade files and update again

.. exception:: ExcCode193

    Controller upgrade files data error: verification failed

    .. method:: solution()

       Copy the upgrade files and update again

.. exception:: ExcCode194

    Controller upgrade files data error: wrong size

    .. method:: solution()

       Copy the upgrade files and update again

.. exception:: ExcCode195

    Controller upgrade files data error: start address

    .. method:: solution()

       Copy the upgrade files and update again

.. exception:: ExcCode196

    Controller upgrade files data error: model not match

    .. method:: solution()

       Copy the upgrade files and update again

.. exception:: ExcCode197

    Controller upgrade files not exist

    .. method:: solution()

       Copy the upgrade files and update again

.. exception:: ExcCode198

    Communication timeout when upgrade the controller

    .. method:: solution()

       check wire connection and update again

.. exception:: ExcCode199

    No USB drive detected

    .. method:: solution()

       Reinsert the USB disk and update again

.. exception:: ExcCode181

    Wrong panel software

    .. method:: solution()

       Update software

.. exception:: ExcCode182

    Panel upgrade files data error: wrong page

    .. method:: solution()

       Copy the upgrade files and update again

.. exception:: ExcCode183

    Panel upgrade files data error: verification failed

    .. method:: solution()

       Copy the upgrade files and update again

.. exception:: ExcCode184

    Panel upgrade files data error: wrong size

    .. method:: solution()

       Copy the upgrade files and update again

.. exception:: ExcCode185

    Panel upgrade files data error: wrong start address

    .. method:: solution()

       Copy the upgrade files and update again

.. exception:: ExcCode186

    Panel upgrade files data error: model not match

    .. method:: solution()

       Copy the upgrade files and update again

.. exception:: ExcCode187

    Panel upgrade files not exist

    .. method:: solution()

       Copy the upgrade files and update again

.. exception:: ExcCode188

    Communication timeout when upgrade the panel

    .. method:: solution()

       check wire connection and update again

.. exception:: ExcCode189

    No USB drive detected

    .. method:: solution()

       Copy the upgrade files and update again

Warning message list
--------------------

.. exception:: ExcCode1

    Pedal warning

    .. method:: solution()

       The pedal must be released when switching on;
       The pedal type must be set correctly when using standing pedal;
       Replace the pedal.

.. exception:: ExcCode2

    Tilt switch warning

    .. method:: solution()

       The warning will be cleared when the machine is back to the normal position;
       Check the tipping sensor on the machine

.. exception:: ExcCode3

    Shortkey warning

    .. method:: solution()

       The short key must be released when switching on

.. exception:: ExcCode4

    Shortkey warning

    .. method:: solution()

       The short key must be released when switching on

.. exception:: ExcCode5

    Bobbin counter warning

    .. method:: solution()

       Replace the bobbin, press back key to clear warning

.. exception:: ExcCode6

    Upper thread breaking warning

    .. method:: solution()

       The upper thread is broken;
       Check the sensor of upper thread.

.. exception:: ExcCode7

    Service counter warning

    .. method:: solution()

       Make a service maintenance, press back key to clear warning

.. exception:: ExcCode8

    Eye protection monitoring

    .. method:: solution()

       Put eye protection cover plate back in place;
       Check the sensor of eye protection.

.. exception:: ExcCode9

    Slide monitoring

    .. method:: solution()

       Close the hook cover plate;
       Check the sensor of slide monitoring;

Information message list
------------------------

.. exception:: ExcCode50

    Oil level is below the minimum level marking

    .. method:: solution()

       Maintenance necessary, see the service instructions for the machine to lubricating the machine

    .. versionchanged:: 90A0-v1.08.05

       Previously, the code of this exception was *10* and belonged to *warning* group.
