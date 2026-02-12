Output configuration
====================

Output ports allow the controller to to drive components on the machine. These
components mainly include various types of electromagnets and solenoid valves.

**All output ports are flexible.** Each output function can be assigned to any available
port using the unified function code table.

.. attention::

    Ensure that each output function is assigned to only one port. Configuring multiple
    output ports for the same function is not permitted and may cause hardware damage or
    logic conflicts.

    The availability of certain output functions depends strictly on the machine head
    type and the installed mechanical components.

.. _output_mode_code_list:

Output Mode Code List
---------------------

The following table lists the available function codes for output port configuration.

- 0 = No function;
- 1 = Thread trimmer;
- 2 = Thread tension;
- 3 = Thread clamp;
- 4 = Reverse;
- 5 = Sewing foot lifter;
- 6 = Stroke;
- 7 = Additional thread tension;
- 8 = Thread wiper(upper);
- 9 = Second stitch length;
- 10 = Needle cooling;
- 11 = Additional knife for short trimmer;
- 12 = Seam center guide;
- 13 = Zero stitch length for short trimmer;
- 14 = Auto corner for 2-needle machine;
- 15 = Puller；
- 16 = Thread wiper(lower);

How to setup the function of output ports?
------------------------------------------

Follow the steps:

1. Confirm which output port is connected to the solenoid valve, like *Output-07* or
   *Output-06*. In this step, you need to know the specific model of the system you are
   using, then refer to its wiring diagram. Refer to the
   :ref:`output_params_quick_reference` section of this chapter to find the parameter
   number that controls the function of this port.
2. Refer to the section at the beginning of this chapter :ref:`output_mode_code_list`,
   get the parameter value you need.
3. Modify the parameter obtained in step 1 to the function code obtained in step 2;
4. Restart the machine to adopt the settings.

Let's take an example:

1. You want set the mode of *Output-01* to the puller;
2. In the parameter list you will find :option:`A71`, which controls the mode of
   *Output-01* :

       A71 = Mode Output-01

3. See the section :ref:`output_mode_code_list`, *15* is code of puller, then change
   :option:`A71` to 15:

       15 = Puller

4. Restart the machine.

.. _output_params_quick_reference:

Quick reference
---------------

This table summarizes which parameter should be used for output configuration:

============== ========== =============
Parameter      Authority  See also
============== ========== =============
Mode Output-01 Technician :option:`A71`
Mode Output-02 Technician :option:`A72`
Mode Output-03 Technician :option:`A73`
Mode Output-04 Technician :option:`A74`
Mode Output-05 Technician :option:`A75`
Mode Output-06 Technician :option:`A76`
Mode Output-07 Technician :option:`A77`
Mode Output-08 Technician :option:`A78`
Mode Output-09 Technician :option:`A79`
Mode Output-10 Technician :option:`A80`
============== ========== =============

Parameter List
--------------

.. option:: A71

    -Max  99
    -Min  0
    -Unit  --
    -Description  Functional assignment for Output-01.

.. option:: A72

    -Max  99
    -Min  0
    -Unit  --
    -Description  Functional assignment for Output-02.

.. option:: A73

    -Max  99
    -Min  0
    -Unit  --
    -Description  Functional assignment for Output-03.

.. option:: A74

    -Max  99
    -Min  0
    -Unit  --
    -Description  Functional assignment for Output-04.

.. option:: A75

    -Max  99
    -Min  0
    -Unit  --
    -Description  Functional assignment for Output-05.

.. option:: A76

    -Max  99
    -Min  0
    -Unit  --
    -Description  Functional assignment for Output-06.

.. option:: A77

    -Max  99
    -Min  0
    -Unit  --
    -Description  Functional assignment for Output-07.

.. option:: A78

    -Max  99
    -Min  0
    -Unit  --
    -Description  Functional assignment for Output-08.

.. option:: A79

    -Max  99
    -Min  0
    -Unit  --
    -Description  Functional assignment for Output-09.

.. option:: A80

    -Max  99
    -Min  0
    -Unit  --
    -Description  Functional assignment for Output-10.
