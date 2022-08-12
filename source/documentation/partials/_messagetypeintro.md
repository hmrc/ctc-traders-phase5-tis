## Message details

Message type details are as follows: 

- Characteristics of the data groups belonging to a message: sequence, number of repetitions, and a status value to indicate if a data group is: 
    - mandatory (R: Required), 
    - optional (O: Optional), or 
    - conditional (D: Dependent).
- Characteristics of the data items belonging to a data group: sequence, number of repetitions, type, length, and a value to indicate if a data item is: 
    - mandatory (R: Required), 
    - optional (O: Optional), or 
    - conditional (D: Dependent).
- Data group nesting is shown with dashes, which means that a data group may contain not only data items but also other groups of data. 
- Links to applicable NCTS code lists. Each link downloads a zip file from a separate non-HMRC site. The code lists are updated regularly. Consider setting up an automated way to download the files regularly and integrate them with your software.
- Links to applicable rules and conditions. 
- Header elements (XML fields that can contain other XML fields) are highlighted in **bold**.

## Accessing the XML schemas

The XML schemas are available for download [here](https://github.com/hmrc/transit-movements-validator/tree/main/conf/xsd).

You can view the XML schema for a particular message type as follows:

1. Navigate to the required message type listed in this section.
1. Under the **XML Root** heading in the table, click the link. 
    
    The selected XML schema is displayed in GitHub.

