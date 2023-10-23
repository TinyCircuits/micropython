BOX2D_MOD_DIR := $(USERMOD_DIR)

CFLAGS_USERMOD += -I$(BOX2D_MOD_DIR)
CFLAGS_USERMOD += -I$(BOX2D_MOD_DIR)/include/

SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/, modbox2d.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, allocate.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, array.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, bitset.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, block_allocator.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, body.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, broad_phase.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, contact.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, contact_solver.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, core.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, distance.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, dynamic_tree.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, geometry.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, hull.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, island.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, joint.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, manifold.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, math.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, mouse_joint.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, pool.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, revolute_joint.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, shape.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, stack_allocator.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, table.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, timer.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, types.c)
SRC_USERMOD += $(addprefix $(BOX2D_MOD_DIR)/src/, world.c)
