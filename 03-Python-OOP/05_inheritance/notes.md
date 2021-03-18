05 Наследяване

# 1 Наследяване

* способност на клас
* способността да наследява методи и пропертита от друг клас
* ползваме за да:
  * преизползваме код
* reuse = преизполва
* superclass = родител (родителски клас)
* subclass
* inheritance

# 2 Метод super()

* метод
* метода връща референция към родителския клас
* извиква / позволява да достъпваме родителски методи
* супер сочи към директния родител
* child class = наследник ? 
* single inheritance
* ```python
        # before py 3.5
        # super(Student, self).__init__(name, age)

        # after py 3.5
        super().__init__(name, age)
* overwriting 
  * създаване на клас в наследника със име
    дублиращо клас в родителя
  * механизъм в други езици, в питон няма тчоно такова 

# 3 Видове наследяване

* child class, parent class
* single inheritance = единично
* multiple inheritance = множествено

# 4 Клас Mixin

* клас без състояние, т.е. без полета
* клас съдържащ само методи
* ползва се да добави функционалност на друг клас
* пример: и колата и часовникът може да пускат радио
  (има се предвид часовник с аларма, която пуска радиото)
* instantiate = инстанциране
    * класът се инстанцира (действие върху класа) = 
    т.е. създава се инстанция на класа
```python
class RadioMixin():
   def play_song_on_station(self, station_frequency):
       return f'playing song on radio frequency {station_frequency}'

class Car(Vehicle, RadioMixin):
    pass

class Clock(RadioMixin):
    pass

```
  










