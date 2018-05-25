## BioLoesSEQ

### Contents
* [How to create a BioLoesSEQ object](#How-to-create-a-BioloesSEQ-object)
* [Representation](#Representation)
* [Function Documentation](#function-documentation)
  * [\_\_init\_\_](#\_\_init\_\_)
  * [reverse_sequence](#reverse_sequence)
  * [upper()](#upper())
  * [lower()](#lower())

### How to create a BioloesSEQ object
To create a BioLoesSEQ object, the file of the module must be imported
```python
from BioLoes import BioLoesSEQ

NewBioLoesObject = BioLoesSEQ(seq, ...)
```

To create a BioLoesSEQ object the following parameters can be given to the object
**Required arguments**
* seq: The sequence of the DNA

 **Optional arguments**
* type_DNA: The type of the DNA (coding or template)

### Representation
#### len()
To get he length of the sequence of the SEQ object. To use this len() function to get the 
length the following code needs to be implemented in your own code:
```python
lengthOfSeq = len(BioLoesSEQ_object)
```
#### str()
To print the object the str() function can be called via the str() function. 
```python
print(str(BioLoesSEQ_object))
```

### Function documentation


#### \_\_init\_\_
This is the constructor function. When creating the BioLoesSEQ object this function is
automatically run to create the object. 

#### reverse_sequence
This function can reverse the sequence, this reversed sequence can then be 
stored in a variable. 
  
For example:
```python
reversedSequence = NewBioLoesSEQObject.reverse_sequence()
```

#### upper()
This function is used to get the upper case sequence. The function will return 
the sequence only

```python
SeqUpper = BioLoesSEQObject.upper()
```

#### lower()
This function is used to get the lower case sequence. The function will retunr the 
sequence only

```python
SeqLower = BioLoesSEQObject.lower()
``` 

