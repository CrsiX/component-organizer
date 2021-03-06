from django.contrib import admin
from django.contrib.auth.models import Group

from backend.models import *


@admin.register(KeyValuePair)
class KeyValuePairAdmin(admin.ModelAdmin):
    list_display = ("key", "value")


@admin.register(Container)
class ContainerModelAdmin(admin.ModelAdmin):
    list_display = ("__str__", "name", "path")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("__str__", "name", "path")


@admin.register(ItemLocation)
class ItemLocationModelAdmin(admin.ModelAdmin):
    list_display = ("parent", "amount", "item")


@admin.register(UniqueItem)
class UniqueItemAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(Resistor)
class ResistorAdmin(admin.ModelAdmin):
    list_display = ("__str__", "resistance", "tolerance", "max_power_dissipation", "mounting")


@admin.register(Potentiometer)
class PotentiometerAdmin(admin.ModelAdmin):
    list_display = ("__str__", "min_resistance", "max_resistance", "tolerance", "max_power_dissipation", "mounting")


@admin.register(Thermistor)
class ThermistorAdmin(admin.ModelAdmin):
    list_display = ("__str__", "thermistor_type", "tolerance", "max_power_dissipation", "mounting")


@admin.register(Varistor)
class VaristorAdmin(admin.ModelAdmin):
    list_display = ("__str__", "breakdown_voltage", "tolerance", "max_power_dissipation", "mounting")


@admin.register(MagnetoResistor)
class MagnetoResistorAdmin(admin.ModelAdmin):
    list_display = ("__str__", "tolerance", "max_power_dissipation", "mounting")


@admin.register(PhotoResistor)
class PhotoResistorAdmin(admin.ModelAdmin):
    list_display = ("__str__", "tolerance", "max_power_dissipation", "mounting")


@admin.register(ShuntResistor)
class ShuntResistorAdmin(admin.ModelAdmin):
    list_display = ("__str__", "max_current", "tolerance", "max_power_dissipation", "mounting")


@admin.register(Capacitor)
class CapacitorAdmin(admin.ModelAdmin):
    list_display = ("__str__", "capacitor_type", "capacitance", "max_voltage", "max_temperature", "mounting")


@admin.register(Fuse)
class FuseAdmin(admin.ModelAdmin):
    list_display = ("__str__", "rated_current", "trigger_characteristics", "mounting")


@admin.register(Wire)
class WireAdmin(admin.ModelAdmin):
    list_display = ("__str__", "length", "diameter")


@admin.register(Transformer)
class TransformerAdmin(admin.ModelAdmin):
    list_display = ("__str__", "transform_ratio", "max_power_dissipation")


@admin.register(Diode)
class DiodeAdmin(admin.ModelAdmin):
    list_display = ("__str__", "name", "diode_type", "breakdown_voltage")


@admin.register(Relay)
class RelayAdmin(admin.ModelAdmin):
    list_display = ("__str__", "max_voltage", "max_current")


admin.site.unregister(Group)
