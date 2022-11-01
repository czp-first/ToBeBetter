# Design Patterns



## 设计原则

### 单一职责原则

就一个类而言，应该仅有一个引起它变化的原因

### 开放-封闭原则

对扩展开放, 对修改封闭

### 依赖倒置原则

要针对接口编程，不要对实现编程

- 高层模块不应该依赖底层模块。两个都应该依赖抽象。
- 抽象不应该依赖细节。细节应该依赖抽象。

### 里式代换原则

子类型必须能够替换掉它们的父类型

### 迪米特法则(LoD)

最少知识原则

如果两个类不必彼此直接通信，那么这两个类就不应当发生直接的相互作用。如果一个类需要调用另一个类的某一个方法的话，可以通过第三者转发这个调用



## 设计模式

<table>
    <tr>
        <td>Patterns</td>
        <td>Pattern</td>
        <td>Desc</td>
    </tr>
    <tr>
        <td rowspan="4">
            <a href='https://github.com/czp-first/ToBeBetter/tree/master/design_pattern/creational'>Creational</a>
        </td>
        <td>
            <a href='https://github.com/czp-first/ToBeBetter/tree/master/design_pattern/creational/factory/factory_method'>factory_method</a>
        </td>
        <td>factory method</td>
    </tr>
    <tr>
        <td>
            <a href='https://github.com/czp-first/ToBeBetter/tree/master/design_pattern/creational/factory/abstract_factory'>abstract_factory</a>
        </td>
        <td>abstract factory</td>
    </tr>
  	<tr>
        <td>
            <a href='https://github.com/czp-first/ToBeBetter/tree/master/design_pattern/creational/builder'>builder</a>
        </td>
        <td>builder</td>
    </tr>
    <tr>
        <td>
            <a href='https://github.com/czp-first/ToBeBetter/tree/master/design_pattern/creational/prototype'>prototype</a>
        </td>
        <td>prototype</td>
    </tr>
    <tr>
        <td rowspan="7">
            <a href='https://github.com/czp-first/ToBeBetter/tree/master/design_pattern/structural'>Structural</a>
        </td>
        <td>
            <a href='https://github.com/czp-first/ToBeBetter/tree/master/design_pattern/structural/adapter'>adapter</a>
        </td>
        <td>adapter</td>
    </tr>
    <tr>
        <td>
            <a href='https://github.com/czp-first/ToBeBetter/tree/master/design_pattern/structural/composite'>decorator</a>
        </td>
        <td>composite</td>
    </tr>
    <tr>
        <td>
            <a href='https://github.com/czp-first/ToBeBetter/tree/master/design_pattern/structural/decorator'>decorator</a>
        </td>
        <td>decorator</td>
    </tr>
  	<tr>
        <td>
            <a href='https://github.com/czp-first/ToBeBetter/tree/master/design_pattern/structural/facade'>facade</a>
        </td>
        <td>facade</td>
    </tr>
    <tr>
        <td>
            <a href='https://github.com/czp-first/ToBeBetter/tree/master/design_pattern/structural/flyweight'>flyweight</a>
        </td>
        <td>flyweight</td>
    </tr>
    <tr>
        <td>
            <a href='https://github.com/czp-first/ToBeBetter/tree/master/design_pattern/structural/mvc'>mvc</a>
        </td>
        <td>mvc</td>
    </tr>
    <tr>
        <td>
            <a href='https://github.com/czp-first/ToBeBetter/tree/master/design_pattern/structural/proxy'>proxy</a>
        </td>
        <td>proxy</td>
    </tr>
    <tr>
        <td rowspan="8">
            <a href='https://github.com/czp-first/ToBeBetter/tree/master/design_pattern/behavioral'>Behavioral</a>
        </td>
        <td>
            <a href='https://github.com/czp-first/ToBeBetter/tree/master/design_pattern/behavioral/chain_of_responsibility'>chain of responsibility</a>
        </td>
        <td>chain of responsibility</td>
    </tr>
    <tr>
        <td>
            <a href='https://github.com/czp-first/ToBeBetter/tree/master/design_pattern/behavioral/command'>command</a>
        </td>
        <td>command</td>
    </tr>
  	<tr>
        <td>
            <a href='https://github.com/czp-first/ToBeBetter/tree/master/design_pattern/behavioral/interpreter'>interpreter</a>
        </td>
        <td>intergreter</td>
    </tr>
    <tr>
        <td>
            <a href='https://github.com/czp-first/ToBeBetter/tree/master/design_pattern/behavioral/memento'>memento</a>
        </td>
        <td>memento</td>
    </tr>
    <tr>
        <td>
            <a href='https://github.com/czp-first/ToBeBetter/tree/master/design_pattern/behavioral/observer'>observer</a>
        </td>
        <td>observer</td>
    </tr>
    <tr>
        <td>
            <a href='https://github.com/czp-first/ToBeBetter/tree/master/design_pattern/behavioral/state'>state</a>
        </td>
        <td>state</td>
    </tr>
    <tr>
        <td>
            <a href='https://github.com/czp-first/ToBeBetter/tree/master/design_pattern/behavioral/strategy'>strategy</a>
        </td>
        <td>strategy</td>
    </tr>
    <tr>
        <td>
            <a href='https://github.com/czp-first/ToBeBetter/tree/master/design_pattern/behavioral/template'>template</a>
        </td>
        <td>template</td>
    </tr>
</table>

# Helpful
- [design_patterns](https://sourcemaking.com/design_patterns)
- [python-patterns](https://github.com/faif/python-patterns)
- [design-patterns](https://refactoringguru.cn/design-patterns)
- 大话设计模式