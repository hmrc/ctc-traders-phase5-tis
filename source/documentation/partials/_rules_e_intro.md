These rules are the technical rules that will be used for the cutover period between 16 and 30 November 2023. During this period, the NCTS phase 4 service will continue running to deal with in-flight transit declarations submitted before 16 November while the phase 5 service will handle all new declarations.

During the cutover period:

- technical rules **with** Transitional Period (TP) measures will be applied to the following message types: 

  - 'Arrival Notification' E_ARR_NOT (IE007)

  - 'Declaration Amendment'  E_DEC_AMD (IE013)

  - 'Declaration Data' E_DEC_DAT (IE015)

  - 'Presentation Notification For The Pre-Lodged Declaration' E_PRE_NOT (IE170)

- technical rules **without** TP measures will be applied to all other message types  defined in this specification

**Note:** 'TPendDate' in a rule refers to 30 November 2023.