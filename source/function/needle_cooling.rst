Needle cooling
==============

Needle cooling can assist in cooling the needle to avoid damage to the sewing material
and breakage of the upper thread.

**Functions:**

Above the speed set by :option:`S18`, the needle cooling start;

Below the speed set by :option:`S18`, the needle cooling does not stop immediately,
needle cooling to continue until the time setted by :option:`T16` has elapsed.

During the follow-up time, if the speed exceeds :option:`S18` again, the needle cooling
start again.

Quick reference
---------------

This table summarizes which parameter should be used for needle cooling:

============================= ========== =============
Parameter                     Authority  See also
============================= ========== =============
Needle Cooling                Operator   :option:`A48`
Needle Cooling Speed          Technician :option:`S18`
Needle Cooling Follow-on Time Technician :option:`T16`
Full power duration           Developer  :option:`O93`
Duty cycle after full power   Developer  :option:`O94`
============================= ========== =============

Parameter List
--------------

.. option:: A48

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Needle cooling function:
      | 0 = Off;
      | 1 = On.

.. option:: S18

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  The needle cooling is activated when sewing speed exceeds this value.

.. option:: T16

    -Max  10
    -Min  0
    -Unit  s
    -Description  Switch-off delay for the needle cooling after the sewing speed drops below the threshold.

.. option:: O93

    -Max  999
    -Min  1
    -Unit  ms
    -Description  Needle cooling: Activation duration in :term:`time period t1` (100% duty cycle).

.. option:: O94

    -Max  100
    -Min  1
    -Unit  %
    -Description  Needle cooling: Duty cycle [%] in :term:`time period t2` .
