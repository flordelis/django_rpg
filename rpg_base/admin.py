from django.contrib import admin
import models


class CharacterLocationRelationshipTab(admin.TabularInline):
    model = models.CharacterLocationRelationship
    extra = 0


@admin.register(models.Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'user',)
    fields = ('name', 'description', 'user',)


class CharacterClassInline(admin.TabularInline):
    fields = ('dnd_class', 'levels')
    model = models.CharacterClass
    extra = 0


@admin.register(models.Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'race', 'campaign', )
    inlines = (
        CharacterClassInline,
        CharacterLocationRelationshipTab,
    )


@admin.register(models.Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_race',)


@admin.register(models.DndClass)
class DndClassAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CharactersInEncounterTab(admin.TabularInline):
    model = models.CharacterInEncounter
    extra = 0


class CharacterIntroducesEncounterTab(admin.TabularInline):
    model = models.CharacterIntroducesEncounter
    extra = 0


class EncounterLocationTab(admin.TabularInline):
    model = models.EncounterLocation
    extra = 0


@admin.register(models.Encounter)
class EncounterAdmin(admin.ModelAdmin):
    list_display = ('name', 'campaign', 'is_running', 'round',)
    inlines = (
        CharacterIntroducesEncounterTab,
        EncounterLocationTab,
        CharactersInEncounterTab,
    )


@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    inlines = (
        CharacterLocationRelationshipTab,
    )


class HitDieTab(admin.TabularInline):
    model = models.HitDie
    extra = 0

@admin.register(models.CharacterTemplate)
class CharacterTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'race', 'user')
    inlines = (
        HitDieTab,
    )
