from libs.codeparser import Parser
from libs.detektor_signature import DetektorSignature


def get_deep_attr(obj, attrs):
    for attr in attrs.split("."):
        obj = getattr(obj, attr)
    return obj


def has_deep_attr(obj, attrs):
    try:
        get_deep_attr(obj, attrs)
        return True
    except AttributeError:
        return False


def set_detektor_signature_on_single_object(obj, filepath_attribute):
    """Set the "detektor_signature" on the object.

    Arguments:
    obj -- The obj that the detektor_signature attribute should be added to.
    filepath_attribute -- The attribute that holds the file path of the code.

    Examples:
    set_detektor_signature_on_single_object(assignment, 'fileobj.path')
    """
    if not has_deep_attr(obj, filepath_attribute):
        raise AttributeError('{} does not exist for {}'.format(filepath_attribute, obj))
    filepath = get_deep_attr(obj, filepath_attribute)
    filehandler = open(filepath, 'r')
    p = Parser('python', filehandler)
    s = p.get_code_signature()
    obj.detektor_signature = DetektorSignature(**s)
    return obj


def set_detektor_signature_on_list_of_objects(object_list, filepath_attribute):
    """Set the "detektor_signature" on a list of objects.

    Arguments:
    object_list -- The list of objects that the detektor_signature attribute should be added to.
    filepath_attribute -- The attribute that holds the file path of the code.

    Examples:
    set_detektor_signature_on_list_of_objects(assignments, 'fileobj.path')
    """
    return [set_detektor_signature_on_single_object(o, filepath_attribute) for o in object_list]


def set_detektor_signature(obj, filepath_attribute):
    """Set the "detektor_signature" on list of, or object.

    Arguments:
    obj -- The obj that the detektor_signature attribute should be added to. Assumed to be iterable.
    filepath_attribute -- The attribute that holds the attribute path.

    Examples:
    set_detektor_signature_on_single_object(assignment, 'fileobj.path')
    """
    try:
        return set_detektor_signature_on_list_of_objects(obj, filepath_attribute)
    except:
        return set_detektor_signature_on_single_object(obj, filepath_attribute)
