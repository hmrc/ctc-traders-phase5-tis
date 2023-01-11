These rules are the technical rules that will be used for the cutover period between 16 and 30 November 2023 during which the NCTS phase 4 service will continue running to deal with in-flight requests submitted before 16 November while the phase 5 service will handle all new requests.

During the cutover period, any technical rules **with** Transitional Period (TP) measures will be applied to: 

- all electronic customs clearance (ECC) messages exchanged among national customs administrations of CTC member countries and with European Commission

- the following ECC message types exchanged between traders and customs offices: 

  - 'Arrival Notification' E_ARR_NOT (IE007)

  - 'Declaration Amendment'  E_DEC_AMD (IE013)

  - 'Declaration Data' E_DEC_DAT (IE015)

  - 'Presentation Notification For The Pre-Lodged Declaration' E_PRE_NOT (IE170)

**Important:** During the cutover period, technical rules **without** TP measures will be applied to all other ECC message types exchanged between traders and customs offices.

**Note:** `<TPendDate>` in a rule refers to 30 November 2023.