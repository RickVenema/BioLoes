## BioLoesSEQ

### How to create a BioloesSEQ object
To create a BioLoesSEQ object, the file of the module must be imported
```python
from BioLoes import BioLoesSEQ

NewBioLoesObject = BioLoesSEQ(seq, type_DNA)
```

To create a BioLoesSEQ object the following parameters can be given to the object
* seq: The sequence of the DNA
* type_DNA: The type of the DNA (coding or template)

### Functions of the BioLoesSEQ object
* [\_\_init\_\_](\_\_init\_\_)
* [reverse_sequence](reverse_sequence)


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

