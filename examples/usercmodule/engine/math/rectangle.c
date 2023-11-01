#include "rectangle.h"
#include "utility/debug_print.h"

// Class required functions
STATIC void rectangle_class_print(const mp_print_t *print, mp_obj_t self_in, mp_print_kind_t kind){
    rectangle_class_obj_t *self = self_in;
    vector2_class_obj_t* pos = MP_OBJ_TO_PTR(self->pos);
    vector2_class_obj_t* size = MP_OBJ_TO_PTR(self->size);
    const mp_float_t px = mp_obj_get_float(pos->x);
    const mp_float_t py = mp_obj_get_float(pos->y);
    const mp_float_t sx = mp_obj_get_float(size->x);
    const mp_float_t sy = mp_obj_get_float(size->y);
    ENGINE_INFO_PRINTF("print(): rectangle [x: %0.3f, y: %0.3f, width: %0.3f, height: %0.3f]", (double)px, (double)py, (double)sx, (double)sy);
}

mp_obj_t rectangle_class_new(const mp_obj_type_t *type, size_t n_args, size_t n_kw, const mp_obj_t *args){
    ENGINE_INFO_PRINTF("New rectangle");

    rectangle_class_obj_t *self = m_new_obj(rectangle_class_obj_t);
    self->base.type = &rectangle_class_type;

    if(n_args == 0) {

      self->base.type = &rectangle_class_type;
      self->pos = vector2_class_new(&vector2_class_type, 0, 0, MP_OBJ_NULL);
      self->size = vector2_class_new(&vector2_class_type, 0, 0, MP_OBJ_NULL);
      // if(!mp_obj_is_type(args[0], &vector2_class_type) || !mp_obj_is_type(args[1], &vector2_class_type)){
      //     mp_raise_TypeError("expected vector arguments");
      // }
      // self->base.type = &rectangle_class_type;
      // self->pos = *((vector2_class_obj_t*)MP_OBJ_TO_PTR(args[0]));
      // self->size = *((vector2_class_obj_t*)MP_OBJ_TO_PTR(args[1]));
    } else {
      mp_raise_TypeError("function takes 0 or 2 arguments");
    }

    return MP_OBJ_FROM_PTR(self);
}

mp_obj_t rectangle_class_copy(const rectangle_class_obj_t *r) {
    rectangle_class_obj_t* ret = m_new_obj(rectangle_class_obj_t);
    ret->base.type = &rectangle_class_type;
    ret->pos = r->pos;
    ret->size = r->size;
    return MP_OBJ_FROM_PTR(ret);
}


// Class methods
STATIC mp_obj_t rectangle_class_area(mp_obj_t self_in){
    const rectangle_class_obj_t* self = MP_OBJ_TO_PTR(self_in);
    vector2_class_obj_t* size = MP_OBJ_TO_PTR(self->size);
    const mp_float_t sx = mp_obj_get_float(size->x);
    const mp_float_t sy = mp_obj_get_float(size->y);
    return mp_obj_new_float(sx * sy);
}
MP_DEFINE_CONST_FUN_OBJ_1(rectangle_class_area_obj, rectangle_class_area);

// Class methods
STATIC mp_obj_t rectangle_class_overlap_test(mp_obj_t self_in, mp_obj_t b_in){
    const rectangle_class_obj_t* self = MP_OBJ_TO_PTR(self_in);
    const rectangle_class_obj_t* b = MP_OBJ_TO_PTR(b_in);
    vector2_class_obj_t* apos = MP_OBJ_TO_PTR(self->pos);
    vector2_class_obj_t* asize = MP_OBJ_TO_PTR(self->size);
    vector2_class_obj_t* bpos = MP_OBJ_TO_PTR(b->pos);
    vector2_class_obj_t* bsize = MP_OBJ_TO_PTR(b->size);
    if(mp_obj_get_float(bpos->x) + mp_obj_get_float(bsize->x) < mp_obj_get_float(apos->x)) return mp_const_false;
    else if(mp_obj_get_float(apos->x) + mp_obj_get_float(asize->x) < mp_obj_get_float(bpos->x)) return mp_const_false;
    else if(mp_obj_get_float(bpos->y) + mp_obj_get_float(bsize->y) < mp_obj_get_float(apos->y)) return mp_const_false;
    else if(mp_obj_get_float(apos->y) + mp_obj_get_float(asize->y) < mp_obj_get_float(bpos->y)) return mp_const_false;
    else return mp_const_true;
}
MP_DEFINE_CONST_FUN_OBJ_2(rectangle_class_overlap_test_obj, rectangle_class_overlap_test);


// Function called when accessing like print(my_node.position.x) (load 'x')
// my_node.position.x = 0 (store 'x').
// See https://micropython-usermod.readthedocs.io/en/latest/usermods_09.html#properties
// See https://github.com/micropython/micropython/blob/91a3f183916e1514fbb8dc58ca5b77acc59d4346/extmod/modasyncio.c#L227
STATIC void rectangle_class_attr(mp_obj_t self_in, qstr attribute, mp_obj_t *destination){
    rectangle_class_obj_t *self = MP_OBJ_TO_PTR(self_in);

    if(destination[0] == MP_OBJ_NULL){          // Load
        switch(attribute) {
            case MP_QSTR_pos:
                destination[0] = self->pos;
                break;
            case MP_QSTR_size:
                destination[0] = self->size;
                break;
            case MP_QSTR_area: destination[0] = MP_OBJ_FROM_PTR(&rectangle_class_area_obj); destination[1] = self_in; break;
            default: break;
        }
    }else if(destination[1] != MP_OBJ_NULL){    // Store
        switch(attribute) {
            case MP_QSTR_pos: self->pos = destination[1]; break;
            case MP_QSTR_size: self->size = destination[1]; break;
            default: return;
        }

        // Success
        destination[0] = MP_OBJ_NULL;
    }
}


// Class attributes
STATIC const mp_rom_map_elem_t rectangle_class_locals_dict_table[] = {
    { MP_ROM_QSTR(MP_QSTR_area), MP_ROM_PTR(&rectangle_class_area_obj) },
    { MP_ROM_QSTR(MP_QSTR_overlap_test), MP_ROM_PTR(&rectangle_class_overlap_test_obj) },
};


// Class init
STATIC MP_DEFINE_CONST_DICT(rectangle_class_locals_dict, rectangle_class_locals_dict_table);

const mp_obj_type_t rectangle_class_type = {
    { &mp_type_type },
    .name = MP_QSTR_Rectangle,
    .print = rectangle_class_print,
    .make_new = rectangle_class_new,
    .call = NULL,
    .unary_op = NULL,
    .binary_op = NULL,
    .attr = rectangle_class_attr,
    .subscr = NULL,
    .getiter = NULL,
    .iternext = NULL,
    .buffer_p = {NULL},
    .locals_dict = (mp_obj_dict_t*)&rectangle_class_locals_dict,
};
