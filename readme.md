## Library Management System 

### Required classes -
- **Book** - Remembering books in library
- **Member** - Represents Library members 
- **Library** - Manages books ,members and transactions 


### Encapsulation - 
- Using Public and private attributes to control access to class 
properties and methods
- Methods within class will be used to add , remove or modify member and book details

### Inheritance - 
- **User** - A base class with attributes like `name`, `id` etc that `Member` will inherit


### Polymorphism - 
- Implemented methods like `borrow_book()` and `return_book()` in a way that 
can be overriden and used by differet classes (`StudentMember`,`FacultyMember`)

### Abstraction  - 
- Hiding the complex logic like book searching and issue in simple methods

