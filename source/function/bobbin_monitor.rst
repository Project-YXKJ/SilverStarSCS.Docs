Bobbin Monitor
==============

Bobbin Monitor is divided into two types: **Bobbin stitch counter (BSC)** and
**Remaining thread monitor (RTM)**, determined by parameter :option:`O99`.

How the alarm works
-------------------

- Warning in the seam (Before Trimming)

  A65 = 0
      The machine does not stop. Sewing continues.

  A65 = 1
      The machine stops, and the display shows :exc:`ExcCode010`, sewing is prohibited.

      After confirming the message on the panel, sewing can resume.

- Warning after thread trimming

  O20 = 0
      The display shows :exc:`ExcCode052`, sewing can continue.

      After manually choosing an appropriate time to replace the bobbin, press reset on
      the panel to restart the counting cycle.

  O20 = 1
      The display shows :exc:`ExcCode005`, Sewing is prohibited.

      After replacing the bobbin, press reset on the panel to restart the counting cycle
      and sewing resumes.

Bobbin stitch counter (BSC)
---------------------------

Using bobbin stitch counter allows users to know the remaining thread amount.

How it works?
~~~~~~~~~~~~~

Here is a formula:

.. math::
    :name: Bobbin Remaining Amount

    N_{\text{Remaining thread amount}}
    = O43_{\text{reset value of the bobbin thread counter}} - O44_{\text{bobbin thread counter value}}

Quick start
~~~~~~~~~~~

Following steps:

1. Set an appropriate value for :option:`O19`, every time N stitches are sewn which set
   by this parameter, the counter value :option:`O44` increases by 1;
2. Set an appropriate value for :option:`O43`, this is a very variable value, which
   depends on the size of the bobbin and the thickness of the thread;
3. Use parameters :option:`A65` and :option:`O20` to determine how the alarm works;
4. Set :option:`A12` to 1, enable the counter.

Remaining thread monitor (RTM)
------------------------------

.. versionchanged:: 90A0-v1.15.03

    Add function.

This function requires an additional sensor, and to avoid signal interference, a
solenoid valve is needed to control the airflow for cleaning the sensor.

Quick start
~~~~~~~~~~~

To activate the remaining thread monitor in the software:

1. Refer to :doc:`input_configuration`, based on the port number connected to the
   sensor, then modify the input function to:

       27 = Sensor (RTM);

2. Refer to :doc:`output_configuration`, based on the port number connected to the
   cleaning air solenoid valve, then modify the output function to:

       17 = Cleaning sensor (RTM);

3. Check in the parameter :option:`O99` if the value is set to 2;
4. Use parameters :option:`A65` and :option:`O20` to determine how the alarm works.
5. Use parameters :option:`A92` and :option:`O93` to determine how the sensor cleaning
   (air blowing) operate;
6. Turn on the sensor cleaning function, parameter :option:`A91` is set to 1.
7. Set :option:`A12` to 1, enable the monitor.

Quick reference
---------------

This table summarizes which parameter should be used for bobbin monitor:

================================= ========== =============
Parameter                         Authority  See also
================================= ========== =============
Bobbin Monitor                    Operator   :option:`A12`
Bobbin Monitor Mode               Operator   :option:`O99`
Sewing stop                       Technician :option:`A65`
Reset necessary                   Technician :option:`O20`
Bobbin Stitch Counter Reset Value Technician :option:`O43`
Bobbin Counter Factor             Technician :option:`O19`
Bobbin Stitch Counter Value       Technician :option:`O44`
Clean (RTM)                       Technician :option:`A91`
Clean Start Stitches (RTM)        Technician :option:`A92`
Clean Time (RTM)                  Technician :option:`A93`
Time (t1)                         Technician :option:`A94`
Duty Cycle (t2)                   Technician :option:`A95`
================================= ========== =============

Parameter List
--------------

.. option:: A12

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Activate the Bobbin stitch counter:
      | 0 = Off;
      | 1 = On.

.. option:: O99

    -Max  2
    -Min  1
    -Unit  --
    -Description
      | Bobbin Monitor Mode:
      | 1 = Software, monitoring of the remaining thread amount by stitch count (BSC);
      | 2 = Monitor, use of the optional sensor remaining thread monitor (RTM).

.. option:: A65

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Sewing stops and a notice is displayed when the bobbin is detected to be nearly empty:
      | 0 = Off;
      | 1 = On.

.. option:: O20

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | When the bobbin is empty after trimming, the sewing is inhibited. A reset is required to resume:
      | 0 = after thread cutting;
      | 1 = immediately.

.. option:: O43

    -Max  9999
    -Min  1
    -Unit  --
    -Description  Bobbin supply capacity. This is a very variable value, which depends
                  on the size of the bobbin and the thickness of the thread.

.. option:: O19

    -Max  200
    -Min  1
    -Unit  stitches
    -Description  Every sew over this number of stitches, increment the counter by 1.

.. option:: O44

    -Max  9999
    -Min  0
    -Unit  --
    -Description  The current value of bobbin stitch counter, the reset value minus
                  this value is remaining value.

.. option:: A91

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Clean (RTM):
      | 0 = Off;
      | 1 = On.

.. option:: A92

    -Max  99
    -Min  0
    -Unit  stitch
    -Description  Clean Start Stitches (RTM):The stitch amount from sewing begin to start sensor cleaning.

.. option:: A93

    -Max  9999
    -Min  1
    -Unit  ms
    -Description  Clean Time (RTM): Duration for which the sensors is blown clear with air flow.

.. option:: A94

    -Max  999
    -Min  1
    -Unit  ms
    -Description  Clean (RTM): Activation duration in :term:`time period t1` (100% duty cycle).

.. option:: A95

    -Max  100
    -Min  1
    -Unit  %
    -Description  Clean (RTM): Duty cycle [%] in :term:`time period t2` .
