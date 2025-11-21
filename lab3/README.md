# **LAB 2 — Structural Design Patterns in RPG Battle Simulator**

### **Author:** Vladislav Amza  
### **Course:** TMPS — Software Design Patterns  
### **Patterns Implemented:** Adapter, Decorator, Facade  

---

# **1. Introduction**

The purpose of this laboratory work was to extend the existing Lab 1 project by implementing **structural design design patterns**, while keeping the overall architecture clean, modular, and extensible.

While Lab 1 introduced **creational patterns** (Builder, Prototype, Singleton), this laboratory work focuses exclusively on **structural design patterns**:

- **Adapter**  
- **Decorator**  
- **Facade**  

The result is a fully interactive **RPG Battle Simulator** using Python and Streamlit, demonstrating how structural patterns simplify complex systems, reduce coupling, and enable clean integration with external interfaces.

---

# **2. Implemented Structural Design Patterns**

## ------------------------------------
## **2.1 Adapter Pattern**
## ------------------------------------

### **Motivation**

The Streamlit GUI provides character data in a JSON-like dictionary format, while the internal domain model expects structured getters like `get_health()`, `get_attack()`, etc.

To decouple UI data format from domain logic, the **Adapter** pattern was introduced.

### **Intent**

Convert an external data structure into an interface compatible with the Builder and Character classes.

### **Implementation**

**File:** `domain/adapter/json_character_adapter.py`

```python
class JSONCharacterAdapter:
    def __init__(self, json_data):
        self._data = json_data

    def get_name(self):
        return self._data["name"]

    def get_health(self):
        return int(self._data["stats"]["health"])

    def get_attack(self):
        return int(self._data["stats"]["attack"])

    def get_speed(self):
        return int(self._data["stats"]["speed"])
```

### **Usage (through Facade)**

```python
adapter = JSONCharacterAdapter(json_data)
character = builder.from_adapter(adapter).build()
```

---

## ------------------------------------
## **2.2 Decorator Pattern**
## ------------------------------------

### **Motivation**

The simulator needed temporary effects such as attack boosts or defensive shields. Instead of modifying the `Character` class directly or creating many subclasses, the **Decorator** pattern allows adding behavior dynamically.

### **Intent**

Attach additional responsibilities to objects at runtime, without altering their structure.

### **Implementation**

**Base Decorator —** `domain/decorator/character_decorator.py`

```python
class CharacterDecorator(Character):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def get_name(self): return self._wrapped.get_name()
    def get_health(self): return self._wrapped.get_health()
    def get_attack(self): return self._wrapped.get_attack()
    def get_speed(self): return self._wrapped.get_speed()

    def take_damage(self, amount): 
        self._wrapped.take_damage(amount)
```

**Example: Attack Boost —** `domain/decorator/attack_boost.py`

```python
class AttackBoost(CharacterDecorator):
    def __init__(self, wrapped, bonus=10):
        super().__init__(wrapped)
        self._bonus = bonus

    def get_attack(self):
        return self._wrapped.get_attack() + self._bonus
```

---

## ------------------------------------
## **2.3 Facade Pattern**
## ------------------------------------

### **Motivation**

The simulator contains multiple moving parts—Builder, Prototype Manager, Singleton GameManager, Adapters, Decorators. To avoid exposing all these components directly to the UI, a **Facade** pattern was implemented to provide a simplified interface.

### **Intent**

Provide a unified interface to a complex subsystem.

### **Implementation**

**File:** `domain/facade/game_facade.py`

```python
class GameFacade:
    def __init__(self):
        self._manager = GameManager()
        self._builder = CharacterBuilder()
        self._prototypes = CharacterPrototypeManager()

    def load_character_from_json(self, slot, json_data):
        adapter = JSONCharacterAdapter(json_data)
        proto = self._prototypes.get_template("warrior")

        character = (
            self._builder
            .from_adapter(adapter)
            .apply_prototype(proto)
            .build()
        )

        self._manager.set_character(slot, character)
        return character

    def apply_attack_boost(self, slot, bonus):
        boosted = AttackBoost(self._manager.get_character(slot), bonus)
        self._manager.set_character(slot, boosted)
        return boosted

    def run_battle_realtime(self, ui_callback):
        return self._manager.simulate_battle_realtime(ui_callback)
```

---

# **3. Streamlit GUI Integration**

A Streamlit-based UI was implemented to provide a real-time, visual demonstration of the structural patterns:

- JSON-based character creation → **Adapter**
- Buff buttons → **Decorator**
- Unified access to subsystems → **Facade**
- Real-time HP bar updates and animated logs

This GUI shows how structural patterns produce clean separation between UI and game logic.

---

# **4. Results**

The final RPG simulator now supports:

- Loading characters from external data formats  
- Applying runtime stat modifiers  
- Running animated real-time battles  
- A clean single entry point for the UI  
- Full separation between UI and internal logic  

Structural patterns greatly improved:
- Flexibility  
- Maintainability  
- Readability  
- Extensibility  

---

# **5. Conclusions**

Structural patterns were successfully integrated into the existing project:

- **Adapter** ensures compatibility with different data formats  
- **Decorator** enables dynamic behavior extension without modifying existing classes  
- **Facade** simplifies interaction by unifying complex subsystems  

These improvements led to a cleaner architecture and a more modular, extensible system.
