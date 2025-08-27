# Pydantic
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json)](https://pydantic.dev)

## 參考資源
- [Pydantic Documentation](https://docs.pydantic.dev/)

## 什麼是 Pydantic?

Pydantic 是透過型態註記 (Type Annotations) 提供資料驗證和設定管理的套件。

## 安裝方式

透過 uv 安裝：

```
uv add pydantic
```

Pydantic 的其他擴充套件：

```
uv add pydantic[email]
uv add pydantic[timezone]
```

## Pydantic 提供的資料型態

```python
import pydantic


# int
pydantic.PositiveInt
pydantic.NegativeInt
pydantic.NonNegativeInt
pydantic.NonPositiveInt

# float
pydantic.PositiveFloat
pydantic.NegativeFloat
pydantic.NonNegativeFloat
pydantic.NonPositiveFloat
pydantic.FiniteFloat

# secret
pydantic.SecretBytes
pydantic.SecretStr

# strict
pydantic.StrictBool
pydantic.StrictBytes
pydantic.StrictFloat
pydantic.StrictInt
pydantic.StrictStr

# constrained
pydantic.conbytes
pydantic.confloat
pydantic.conint
pydantic.condecimal
pydantic.constr
pydantic.conlist
pydantic.conset
pydantic.confrozenset
pydantic.condate

# path
pydantic.FilePath
pydantic.DirectoryPath
pydantic.NewPath

# url
pydantic.AnyUrl
pydantic.AnyHttpUrl
pydantic.FileUrl
pydantic.HttpUrl
pydantic.FtpUrl
pydantic.WebsocketUrl
pydantic.AnyWebsocketUrl
pydantic.UrlConstraints

# email
pydantic.EmailStr
pydantic.NameEmail
pydantic.validate_email

# ip
pydantic.IPvAnyAddress
pydantic.IPvAnyInterface
pydantic.IPvAnyNetwork
```

## Pydantic 常用的類別和方法

```python
import pydantic
import pydantic_core


# main
pydantic.BaseModel
pydantic.create_model

# type_adapter
pydantic.TypeAdapter

# fields
pydantic.Field
pydantic.computed_field

# alias
pydantic.AliasChoices
pydantic.AliasGenerator
pydantic.AliasPath
pydantic.alias_generators

# config
pydantic.ConfigDict

# validate_call
pydantic.validate_call

# functional_validators
pydantic.InstanceOf
pydantic.AfterValidator
pydantic.BeforeValidator
pydantic.PlainValidator
pydantic.WrapValidator
pydantic.field_validator
pydantic.model_validator

# functional_serializers
pydantic.PlainSerializer
pydantic.WrapSerializer
pydantic.field_serializer
pydantic.model_serializer

# json_schema
pydantic.WithJsonSchema

# pydantic_core
pydantic.ValidationError
pydantic.ValidationInfo
pydantic_core.PydanticCustomError
pydantic_core.PydanticUseDefault
pydantic_core.from_json

# pydantic_settings
pydantic_settings.BaseSettings
pydantic_settings.SettingsConfigDict
pydantic_settings.SettingsError
pydantic_settings.CliMutuallyExclusiveGroup
pydantic_settings.CliSubCommand
pydantic_settings.CliApp
pydantic_settings.CliPositionalArg
pydantic_settings.CliUnknownArgs
pydantic_settings.CliImplicitFlag
pydantic_settings.CliExplicitFlag
pydantic_settings.get_subcommand
```

## 透過 BaseModel 驗證資料

- 使用 `BaseModel` 來定義資料模型。
    - 若使用 `ClassVar` 為資料型態，建立實例會將 `ClassVar` 當成 class variables，不作為欄位，序列化也不輸出；但重新指派新值時，則會引發錯誤。
    - 若使用屬性名稱前帶有一個底線符號 (_)，建立實例會將其當成 private attributes，不作為欄位，序列化也不輸出；重新指派新值時，不會引發錯誤。
    - 使用 `model_post_init()` 來進行後置初始化，而非使用 `__init__()`。這個方法會在實例化後被呼叫，可以用來修改欄位值或進行其他初始化操作。
    ```python
    import json
    from typing import ClassVar

    from pydantic import BaseModel, ValidationError


    class EmployeeModel(BaseModel):
        country: ClassVar[str] = "Taiwan"

        _secret_value: int = 7

        name: str
        salary: int

        def model_post_init(self, __context: object) -> None:
            self.salary += 10


    print(employee._secret_value)
    #> 7
    employee._secret_value = 9
    print(employee._secret_value)
    #> 9

    # 建立一個正確實例
    employee = EmployeeModel(
        name="Bar",
        salary=1000,
    )
    print(employee.model_dump())
    #> {'name': 'Bar', 'salary': 1010}

    # 建立一個錯誤的實例，設定 country 為 ClassVar
    employee2 = EmployeeModel(
        name="Bar",
        salary=1000,
        country="Japan"
    )
    print(employee2.model_dump())
    #> {'name': 'Bar', 'salary': 1010}
    print(employee2.country)
    #> Taiwan

    # 建立一個錯誤的實例，會引發錯誤
    try:
        employee3 = EmployeeModel(
            name="Bar",
            salary="secret",
        )
    except ValidationError as e:
        # 其中 e.errors() 會回傳一個 list[dict[str, Any]]
        errs = e.errors()
        print(json.dumps(errs, indent=4))
        """
        [
            {
                "type": "int_parsing",
                "loc": [
                    "salary"
                ],
                "msg": "Input should be a valid integer, unable to parse string as an integer",
                "input": "secret",
                "url": "https://errors.pydantic.dev/2.11/v/int_parsing"
            }
        ]
        """
    ```
- 輸出 Model 的 JSON schema。
    <details>
    <summary>JSON schema</summary>

    ```python
    import json


    print(json.dumps(EmployeeModel.model_json_schema(), indent=4))
    """
    {
        "properties": {
            "name": {
                "title": "Name",
                "type": "string"
            },
            "salary": {
                "title": "Salary",
                "type": "integer"
            },
            "age": {
                "anyOf": [
                    {
                        "type": "integer"
                    },
                    {
                        "type": "null"
                    }
                ],
                "default": null,
                "title": "Age"
            }
        },
        "required": [
            "name"
        ],
        "title": "EmployeeModel",
        "type": "object"
    }
    """
    ```
    </details>
- 序列化輸出 Model 為特定格式。
    ```python
    from pydantic import BaseModel


    class EmployeeModel(BaseModel):
        name: str
        salary: float | None = None
        age: int | None = None

    employee = EmployeeModel(
        name="Bar",
        salary=1000,
    )

    print(employee.model_dump())    # 轉換為 dict
    #> {'name': 'Bar', 'salary': 1000.0, 'age': None}

    print(employee.model_dump(exclude="name"))    # 轉換為 dict，但序列化不輸出指定的欄位
    #> {'salary': 1000.0, 'age': None}

    print(employee.model_dump(exclude_unset=True))    # 轉換為 dict，但序列化不輸出未設定的欄位
    #> {'name': 'Bar', 'salary': 1000.0}

    print(employee.model_dump(exclude_defaults=True))    # 轉換為 dict，但序列化不輸出預設值的欄位
    #> {'name': 'Bar', 'salary': 1000.0}

    print(employee.model_dump(mode="json"))    # 轉換為 dict 的 json 模式
    #> {'name': 'Bar', 'salary': 1000.0, 'age': None}

    print(employee.model_dump_json())    # 轉換為 json
    #> '{"name":"Bar","salary":1000.0,"age":null}'
    ```
- 使用 `model_validate()` 或 `model_validate_json()` 驗證資料。
    ```python
    import json

    from pydantic import BaseModel, ValidationError


    class EmployeeModel(BaseModel):
        name: str
        salary: float | None = None

    try:
        employee_dict = EmployeeModel.model_validate(    # 驗證資料為 dict
            {
                "name": "Bar",
                "salary": 1000,
            }
        )

        employee_json = EmployeeModel.model_validate_json(    # 驗證資料為 json
            '{"name": "Bar", "salary": 1000}'
        )

        employee_strings = EmployeeModel.model_validate_strings(    # 驗證資料為 dict[str, str]
            {
                "name": "Bar",
                "salary": "1000",
            }
        )
    except ValidationError as e:
        errs = e.errors()
        print(json.dumps(errs, indent=4))
    ```
- 透過泛型定義資料模型 (以下寫法適用於包含 Python 3.12 和以上的版本)。
    - 使用 `model_parametrized_name()` 來取代 Model 的 `__name__` 屬性。
    ```python
    from typing import Any, TypeVar

    from pydantic import BaseModel, ValidationError


    class DataModel(BaseModel):
        number: int


    class Response[DataT](BaseModel):
        data: DataT


    class Response2[DataT](BaseModel):
        data: DataT

        @classmethod
        def model_parametrized_name(cls, params: tuple[type[Any]]) -> str:
            return f'{params[0].__name__.title()}Response'


    print(Response[int](data=1))
    #> data=1
    print(Response[str](data='value'))
    #> data='value'
    print(Response[str](data='value').model_dump())
    #> {'data': 'value'}

    print(repr(Response[int](data=1)))
    #> Response[int](data=1)
    print(repr(Response[str](data='value')))
    #> Response[str](data='value')

    print(repr(Response2[int](data=1)))
    #> IntResponse(data=1)
    print(repr(Response2[str](data='value')))
    #> StrResponse(data='value')

    data = DataModel(number=1)
    print(Response[DataModel](data=data).model_dump())
    #> {'data': {'number': 1}}
    try:
        Response[int](data='value')
    except ValidationError as e:
        print(e)
        """
        1 validation error for Response[int]
        data
        Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='value', input_type=str]
        """
    ```


## 透過 Field 建立欄位規則

- 使用 `Field` 來定義欄位規則。
    - 數值欄位限制
        - 使用 `gt`、 `ge`、`lt`、`le` 來定義數值的大小限制。
        - 使用 `multiple_of` 來定義數值的倍數限制。
        - 使用 `allow_inf_nan` 來允許無窮大和 NaN 值。
        - 使用 `max_digits` 來限制數值的最大位數。
        - 使用 `decimal_places` 來限制數值的小數位數。
    - 字串欄位限制
        - 使用 `min_length`、`max_length` 來定義字串的長度限制。
        - 使用 `pattern` 來定義字串的正則表達式限制。
    - dataclasses 限制
        - 使用 `init` 來定義類別需要包含初始化方法。
        - 使用 `init_var` 來定義類別只會被初始化，但不會被視為欄位。
        - 使用 `kw_only` 來定義類別的關鍵字參數。
    - 其他限制
        - 使用 `default`、`default_factory` 來定義欄位的預設值。
            - 使用 `validate_default=True` 來啟用驗證預設值，預設不會驗證預設值。
            - `default_factory` 中的參數 `data` 只能使用已驗證過的資料。
        - 使用 `strict` 來定義欄位為嚴格模式，不允許自動轉換資料型態。
            - [Conversion Table](https://docs.pydantic.dev/latest/concepts/conversion_table/)
        - 使用 `frozen` 來定義欄位不可重新指派。
        - 使用 `exclude` 來定義欄位在序列化輸出時被排除。
        - 使用 `repr` 來定義欄位不會被 print 出來。
    ```python
    from pydantic import BaseModel, Field


    class EmployeeModel(BaseModel):
        name: str
        salary: float | None = Field(default=None, gt=0)
        age: int | None = Field(default=None, ge=0)
        secret: str = Field(default_factory=lambda data: data["name"]*2)


    employee = EmployeeModel(
        name="Bar",
        salary=1000,
        age=30
    )
    print(employee.model_dump())
    #> {'name': 'Bar', 'salary': 1000.0, 'age': 30, 'secret': 'BarBar'}
    ```
- 使用 `@field_validator` 來實作單一欄位驗證。
    - `@field_validator` 的參數是欄位名稱，且可以輸入多個欄位名稱。
    - 若使用 `@field_validator("*")`，則會驗證所有欄位。
    - 也可以使用 `AfterValidator` 來實作欄位驗證。
    - 當定義多個 `AfterValidator`、`BeforeValidator`、`WrapValidator` 時，`AfterValidator` 會依照定義的順序由左至右依序執行，而 `BeforeValidator`、`WrapValidator` 會依照定義的順序由右至左依序執行。
    ```python
    import re

    from pydantic import AfterValidator, BaseModel, Field, field_validator


    class EmployeeModel(BaseModel):
        name: str
        salary: float | None = Field(default=None, gt=0)
        age: int | None = Field(default=None, ge=0)

        @field_validator("name", mode="after")
        @classmethod
        def name_should_contain_at_least_one_letter(cls, value: str) -> str:
            """Name should contain at least one letter."""
            if not re.search(r"[a-zA-Z]", value):
                raise ValueError("Name should contain at least one letter")
            return value


    def name_should_contain_at_least_one_letter(value: str) -> str:
        """Name should contain at least one letter."""
        if not re.search(r"[a-zA-Z]", value):
            raise ValueError("Name should contain at least one letter")
        return value


    class EmployeeModel2(BaseModel):
        name: Annotated[str, AfterValidator(name_should_contain_at_least_one_letter)]
        salary: float | None = Field(default=None, gt=0)
        age: int | None = Field(default=None, ge=0)

    ```
- 使用 `@model_validator` 來實作跨欄位驗證。
    - 參數 `mode` 可以是 `before`、`after` 或 `wrap`。
    ```python
    from typing import Self

    from pydantic import BaseModel, Field, model_validator


    class UserModel(BaseModel):
        username: str
        password: str = Field(min_length=8)
        confirm_password: str = Field(min_length=8)

        @model_validator(mode="after")
        def passwords_should_match(self) -> Self:
            """Passwords should match."""
            if self.password != self.confirm_password:
                raise ValueError("Passwords should match")
            return self
    ```
- 使用 `@computed_field` 來定義計算欄位。
    ```python
    from pydantic import BaseModel, Field, computed_field


    class AreaModel(BaseModel):
        width: int = Field(gt=0)
        height: int = Field(gt=0)

        @computed_field
        @property
        def area(self) -> int:
            """Calculate the area."""
            return self.width * self.height


    area = AreaModel(width=5, height=10)
    print(area.model_dump())
    #> {'width': 5, 'height': 10, 'area': 50}
    ```

## Model 設定檔

- 若提供 Model 未定義的欄位時，會被忽略不會引發錯誤，並且使用 `model_dump()` 序列化輸出時也會忽略定義以外的欄位。
    - 若要 Model 包含未定義的欄位，需要在 `ConfigDict` 中設定 `extra="allow"`。
    - 未定義的欄位會儲存在 `__pydantic_extra__` 屬性中。
    ```python
    from pydantic import BaseModel, ConfigDict


    class Model(BaseModel):
        model_config = ConfigDict(extra="allow")    # ["allow", "ignore", "forbid"]

        x: int

    m = Model(x=1, y=2)
    assert m.model_dump() == {"x": 1, "y": 2}
    assert m.__pydantic_extra__ == {"y": 2}
    ```
- 若要建立欄位不可重新指派的實例，需要在 `ConfigDict` 中設定 `frozen=True`。
    - 但若是修改 list 或 dict 等物件中的值，則不會引發錯誤。
    ```python
    from pydantic import BaseModel, ConfigDict


    class Model(BaseModel):
        model_config = ConfigDict(frozen=True)

        x: int
        y: dict[str, str]

    m = Model(x=1, y={"b": "apple"})
    try:
        m.x = 2
    except ValidationError as e:
        print(e)
        """
        1 validation error for Model
        x
        Instance is frozen [type=frozen_instance, input_value=2, input_type=int]
        """

    m.y["b"] = "banana"
    print(m.model_dump())
    #> {'x': 1, 'y': {'b': 'banana'}}
    ```
- 若在建立實例後，某個欄位被指派新值時，重新驗證欄位，則需要在 `ConfigDict` 中設定 `validate_assignment=True`。
- 若在建立實例後，因沒有設定 `validate_assignment=True` 且某個欄位被指派新值時，再以該實例建立新的 Model，重新驗證該實例，則需要在 `ConfigDict` 中設定 `revalidate_instances="always"`。
- 預設只允許內建的資料型態，若要使用第三方資料型態，則需要在 `ConfigDict` 中設定 `arbitrary_types_allowed=True`。或是使用 `InstanceOf` 來定義欄位型態。
    ```python
    from ipaddress import IPv4Address

    import paramiko
    from pydantic import BaseModel, ConfigDict, Field, InstanceOf, field_validator


    class SSHClient(BaseModel):
        """SSH client class for paramiko-based SSH operations.

        This class provides methods for connecting to an SSH server, running commands,
        and managing connection parameters.

        Attributes:
            host (IPv4Address): The SSH server host (IPv4).
            port (int): The SSH server port.
            username (str): The SSH username.
            password (str): The SSH password.
            client (paramiko.SSHClient): The paramiko SSH client instance.
            exit_status (int | None): Previous exit status of run method.
        """

        model_config = ConfigDict(
            arbitrary_types_allowed=True,
            validate_assignment=True,
            revalidate_instances="always",    # ["always", "never", "subclass-instances"]
        )

        host: str
        port: int = Field(default=22, ge=1, le=65535)
        username: str
        password: str
        client: paramiko.SSHClient = Field(default_factory=paramiko.SSHClient)
        exit_status: int | None = Field(default=None, description="Previous exit status of run method")

        @field_validator("host")
        @classmethod
        def validate_host(cls, value: str) -> str:
            """Validate and convert host to IPv4Address."""
            if not IPv4Address(value):
                raise ValueError("Invalid IPv4 address")
            return value

    class SSHClient2(BaseModel):
        """SSH client class for paramiko-based SSH operations.

        This class provides methods for connecting to an SSH server, running commands,
        and managing connection parameters.

        Attributes:
            host (IPv4Address): The SSH server host (IPv4).
            port (int): The SSH server port.
            username (str): The SSH username.
            password (str): The SSH password.
            client (paramiko.SSHClient): The paramiko SSH client instance.
            exit_status (int | None): Previous exit status of run method.
        """

        model_config = ConfigDict(
            validate_assignment=True,
            revalidate_instances="always",    # ["always", "never", "subclass-instances"]
        )

        host: str
        port: int = Field(default=22, ge=1, le=65535)
        username: str
        password: str
        client: InstanceOf[paramiko.SSHClient] = Field(default_factory=paramiko.SSHClient)
        exit_status: int | None = Field(default=None, description="Previous exit status of run method")

        @field_validator("host")
        @classmethod
        def validate_host(cls, value: str) -> str:
            """Validate and convert host to IPv4Address."""
            if not IPv4Address(value):
                raise ValueError("Invalid IPv4 address")
            return value
    ```

## 將 JSON 轉換為 dict

- 透過 `from_json()` 將 JSON 資料轉換為 dict。
    - 使用 `allow_partial` 參數來允許不完整的 JSON 內容。
    - 比 `json.loads()` 的效能要好。
    ```python
    from pydantic_core import from_json


    try:
        employee = from_json('{"name": "Bar", "salary":', allow_partial=False)
    except ValueError as e:
        print(e)
        employee = from_json('{"name": "Bar", "salary":', allow_partial=True)
        print(employee)
        #{'name': 'Bar'}
    ```

## 透過 pydantic_settings 進行設定管理

- 使用 `pydantic_settings.BaseSettings` 來定義設定模型。
- 使用 `pydantic_settings.SettingsConfigDict` 來配置環境變數檔案及其他選項。

### Dotenv 範例

    ```
    # .env
    TEST_VAR=test
    ```

    ```python
    from pydantic_settings import BaseSettings, SettingsConfigDict


    class Settings(BaseSettings):
        model_config = SettingsConfigDict(
            env_file=".env",
            env_file_encoding="utf-8",
            extra="allow",    # ["allow", "ignore", "forbid"]
        )

    settings = Settings()
    settings = Settings(_env_file=".env", _env_file_encoding="utf-8")
    print(settings)
    #> test_var='test'
    ```

### Command Line 範例

    ```python
    import sys

    from pydantic_settings import BaseSettings, SettingsConfigDict, SettingsError


    class Settings(BaseSettings):
        model_config = SettingsConfigDict(
            cli_parse_args=True,
            cli_exit_on_error=False,
        )

        test_var: str | None = None


    sys.argv = ["main.py", "--test_var=test"]

    try:
        settings = Settings()
        print(settings)
        #> test_var='test'
    except SettingsError as e:
        print(e)
    ```
