static void mp_machine_idle(void) {
    
}

static mp_obj_t mp_machine_unique_id(void){
    uint8_t id[8] = {0, 0, 0, 0, 0, 0, 0, 0}; 
    return mp_obj_new_bytes(id, sizeof(id));
}


static mp_obj_t mp_machine_get_freq(void){
    return mp_obj_new_int(0);
}

static void mp_machine_set_freq(size_t n_args, const mp_obj_t *args){
    return;
}

static void mp_machine_lightsleep(size_t n_args, const mp_obj_t *args){
    return;
}

NORETURN static void mp_machine_deepsleep(size_t n_args, const mp_obj_t *args){
    while(1){};
}