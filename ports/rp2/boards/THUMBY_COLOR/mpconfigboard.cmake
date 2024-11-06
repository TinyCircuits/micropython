# cmake file for Raspberry Pi Pico2
#set(PICO_BOARD "pico2")

# To change the gpio count for QFN-80
# set(PICO_NUM_GPIOS 48)

list(APPEND PICO_BOARD_HEADER_DIRS ${MICROPY_BOARD_DIR})
set(MICROPY_C_HEAP_SIZE 100000)