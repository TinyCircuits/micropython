ENGINE_MOD_DIR := $(USERMOD_DIR)

# Add our source files to the respective variables.
SRC_USERMOD += $(ENGINE_MOD_DIR)/engine.c
SRC_USERMOD += $(ENGINE_MOD_DIR)/nodes/empty_node.c
SRC_USERMOD += $(ENGINE_MOD_DIR)/utility/linked_list.c
SRC_USERMOD += $(ENGINE_MOD_DIR)/engine_object_layers.c
SRC_USERMOD += $(ENGINE_MOD_DIR)/display/engine_display.c
SRC_USERMOD += $(ENGINE_MOD_DIR)/display/engine_display_sdl.c

# We can add our module folder to include paths if needed
# This is not actually needed in this example.
CFLAGS_USERMOD += -I$(ENGINE_MOD_DIR)
LDFLAGS_EXTRA += -lSDL2
CEXAMPLE_MOD_DIR := $(USERMOD_DIR)