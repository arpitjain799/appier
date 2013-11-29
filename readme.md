# Appier

Simple WSGI based framework for easy REST API creation.

## Example

```python
import appier

class HelloApp(appier.App):

    def __init__(self):
        appier.App.__init__(self, name = "hello")

    @appier.route("/hello", "GET")
    def hello(self):
        return dict(
            message = "hello world"
        )

    @appier.route("/hello/<int:count>", "GET")    
    def hello_count(self, count):
        return dict(
            message = "hello world %d" % count
        )

    @appier.route("/hello.tpl", "GET")
    def hello_template(self):
        return self.template("hello.txt", message = "hello world")

app = HelloApp()
app.serve()
```

## Data Model

### Attributes

* `type` - The data type to be used for the attribute
* `index` - Boolean indicating if the attribute should be indexex in the data source
* `increment` - Flag tha defines if the (integer based) attribute should be incremented on create
* `secure` - Indicates if the attribute should not be set on the build operation (security setting)

### Types

* `str` - The string type for text fields (this is the default type)
* `int` - Number type to be used for integer values
* `float` - Floating point type for real values
* `appier.File` - Type to be used for referncing file objects
* `appier.reference` -
* `appier.references` -

### Example

```python
import appier

class Account(appier.Model):

    id = dict(
        index = True,
        increment = True
    )

    username = dict(
        index = True
    )

    email = dict(
        index = True
    )

    password = dict(
        private = True
    )
    
    age = dict(
        type = int
    )
```
