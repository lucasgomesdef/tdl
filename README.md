# tdl
Command Line Todo List

### Install using git
Clone repository
```
git clone https://github.com/lucasgomesdef/tdl.git ~/.tdl
```

Create alias into your favorite rc. Ex: (zshrc)
```
echo "alias tdl='python3 ~/.tdl/tdl.py'" >> ~/.zshrc
```

Source the rc
```
source ~/.zshrc
```

### Usage

```
tdl [cmd] <parameters>
```
Commands:
* [**list**]: List all todo list items;
* [**add**] *description*: Add todo list item with given *description*;
* [**remove**] *id*: Remove todo list item with given *id*;
* [**done**] *id*: Mark todo list item with given *id* as done;
* [**undone**] *id*: Mark todo list item with given *id* as undone;
* [**clear**]: Clear all todo list items;
