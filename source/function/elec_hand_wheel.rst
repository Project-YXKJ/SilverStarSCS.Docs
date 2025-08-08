Electric Handwheel
==================

This function can only be used when the motor is stopped.

Handwheel Rotation by button
----------------------------

The handwheel can be set in motion by pressing a button. Select the input port used for
this function.

When the key is pressed **briefly**, i.e. release immediately , the handwheel rotates by
the steps set using parameter :option:`O83`.

When the button is **held down**, the handwheel rotates continuously until the key is
released. The handwheel rotates at the speed set using parameter :option:`O84`.

Quick reference
---------------

This table summarizes which parameter should be used for electric handwheel:

==================================== ========== =============
Parameter                            Authority  See also
==================================== ========== =============
Elec-Handwheel                       Operator   :option:`A23`
Rotation Direction of Elec-Handwheel Technician :option:`A43`
Elec-Handwheel Step                  Technician :option:`O83`
Elec-Handwheel Speed                 Technician :option:`O84`
==================================== ========== =============

Parameter List
--------------

.. option:: A23

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Electronic handwheel:
      | 0 = Off;
      | 1 = On.

.. option:: A43

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Rotation direction of electronic handwheel:
      | 0 = Same with main motor;
      | 1 = Contrary.

.. option:: O83

    -Max  720
    -Min  0
    -Unit  --
    -Description  Step width for electronic handwheel.

.. option:: O84

    -Max  200
    -Min  0
    -Unit  spm
    -Description  The speed of motor when using electric handwheel.
