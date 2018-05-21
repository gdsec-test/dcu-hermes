# OCM Client

This library serves as a limited interface for interacting with the OCM system. It provides basic validation around templates and their expected values.

## Cloning

Cloning the project can be achieved via

```
git clone git@github.secureserver.net:ITSecurity/ocm-client.git
```

## Installing Dependencies
You can install the required public dependencies via 
```
pip install -r requirements.txt
```

## Installing
To install the OCM Client library, you can use the following command
```
pip install git+ssh//git@github.secureserver.net/ITSecurity/ocm-client.git
```
or `pip install .` after cloning the repository.


## Testing
You must install the required dependencies to run tests via
```
pip install -r test_requirements.txt
```

After this you may run the tests via
```
nosetests --with-coverage --cover-package=ocm-client
```