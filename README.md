# md-follow

Follow links in markdown creation.

## Usage

First, install packages dependencies. Go to the root project folder and install it:

```
pip install -r requirements.txt
```

Second, install the package itself:

```
pip install .
```

Finally, you can use it. Go to a directiry which have a `README.md` file and type:

```
mdfollow
```

Optionally, you may want to create a documentation folder to exclusivelly deposity the new generated file. If so, just do:

```
mdfollow --documentation-folder
```

You can add a title to the document

```
mdfollow --title "My Document Title"
```
