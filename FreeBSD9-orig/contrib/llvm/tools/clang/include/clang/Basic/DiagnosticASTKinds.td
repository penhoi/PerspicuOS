//==--- DiagnosticASTKinds.td - libast diagnostics ------------------------===//
//
//                     The LLVM Compiler Infrastructure
//
// This file is distributed under the University of Illinois Open Source
// License. See LICENSE.TXT for details.
//
//===----------------------------------------------------------------------===//

let Component = "AST" in {

//def note_comma_in_ice : Note<
//  "C does not permit evaluated commas in an integer constant expression">;
def note_expr_divide_by_zero : Note<"division by zero">;

// inline asm related.
let CategoryName = "Inline Assembly Issue" in {
  def err_asm_invalid_escape : Error<
    "invalid %% escape in inline assembly string">;
  def err_asm_unknown_symbolic_operand_name : Error<
    "unknown symbolic operand name in inline assembly string">;

  def err_asm_unterminated_symbolic_operand_name : Error<
    "unterminated symbolic operand name in inline assembly string">;
  def err_asm_empty_symbolic_operand_name : Error<
    "empty symbolic operand name in inline assembly string">;
  def err_asm_invalid_operand_number : Error<
    "invalid operand number in inline asm string">;
}


// Importing ASTs
def err_odr_variable_type_inconsistent : Error<
  "external variable %0 declared with incompatible types in different "
  "translation units (%1 vs. %2)">;
def err_odr_variable_multiple_def : Error<
  "external variable %0 defined in multiple translation units">;
def note_odr_value_here : Note<"declared here with type %0">;
def note_odr_defined_here : Note<"also defined here">;
def err_odr_function_type_inconsistent : Error<
  "external function %0 declared with incompatible types in different "
  "translation units (%1 vs. %2)">;
def warn_odr_tag_type_inconsistent : Warning<
  "type %0 has incompatible definitions in different translation units">;
def note_odr_tag_kind_here: Note<
  "%0 is a %select{struct|union|class|enum}1 here">;
def note_odr_field : Note<"field %0 has type %1 here">;
def note_odr_missing_field : Note<"no corresponding field here">;
def note_odr_bit_field : Note<"bit-field %0 with type %1 and length %2 here">;
def note_odr_not_bit_field : Note<"field %0 is not a bit-field">;
def note_odr_base : Note<"class has base type %0">;
def note_odr_virtual_base : Note<
  "%select{non-virtual|virtual}0 derivation here">;
def note_odr_missing_base : Note<"no corresponding base class here">;
def note_odr_number_of_bases : Note<
  "class has %0 base %plural{1:class|:classes}0">;
def note_odr_enumerator : Note<"enumerator %0 with value %1 here">;
def note_odr_missing_enumerator : Note<"no corresponding enumerator here">;

def err_odr_field_type_inconsistent : Error<
  "field %0 declared with incompatible types in different "
  "translation units (%1 vs. %2)">;

// Importing Objective-C ASTs
def err_odr_ivar_type_inconsistent : Error<
  "instance variable %0 declared with incompatible types in different "
  "translation units (%1 vs. %2)">;
def err_odr_objc_superclass_inconsistent : Error<
  "class %0 has incompatible superclasses">;
def note_odr_objc_superclass : Note<"inherits from superclass %0 here">;
def note_odr_objc_missing_superclass : Note<"no corresponding superclass here">;
def err_odr_objc_method_result_type_inconsistent : Error<
  "%select{class|instance}0 method %1 has incompatible result types in "
  "different translation units (%2 vs. %3)">;
def err_odr_objc_method_num_params_inconsistent : Error<
  "%select{class|instance}0 method %1 has a different number of parameters in "
  "different translation units (%2 vs. %3)">;
def err_odr_objc_method_param_type_inconsistent : Error<
  "%select{class|instance}0 method %1 has a parameter with a different types "
  "in different translation units (%2 vs. %3)">;
def err_odr_objc_method_variadic_inconsistent : Error<
  "%select{class|instance}0 method %1 is variadic in one translation unit "
  "and not variadic in another">;
def note_odr_objc_method_here : Note<
  "%select{class|instance}0 method %1 also declared here">;
def err_odr_objc_property_type_inconsistent : Error<
  "property %0 declared with incompatible types in different "
  "translation units (%1 vs. %2)">;
def err_odr_objc_property_impl_kind_inconsistent : Error<
  "property %0 is implemented with %select{@synthesize|@dynamic}1 in one "
  "translation but %select{@dynamic|@synthesize}1 in another translation unit">;
def note_odr_objc_property_impl_kind : Note<
  "property %0 is implemented with %select{@synthesize|@dynamic}1 here">;
def err_odr_objc_synthesize_ivar_inconsistent : Error<
  "property %0 is synthesized to different ivars in different translation "
  "units (%1 vs. %2)">;
def note_odr_objc_synthesize_ivar_here : Note<
  "property is synthesized to ivar %0 here">;

// Importing C++ ASTs
def err_odr_different_num_template_parameters : Error<
  "template parameter lists have a different number of parameters (%0 vs %1)">;
def note_odr_template_parameter_list : Note<
  "template parameter list also declared here">;
def err_odr_different_template_parameter_kind : Error<
  "template parameter has different kinds in different translation units">;
def note_odr_template_parameter_here : Note<
  "template parameter declared here">;
def err_odr_parameter_pack_non_pack : Error<
  "parameter kind mismatch; parameter is %select{not a|a}0 parameter pack">;
def note_odr_parameter_pack_non_pack : Note<
  "%select{parameter|parameter pack}0 declared here">;
def err_odr_non_type_parameter_type_inconsistent : Error<
  "non-type template parameter declared with incompatible types in different "
  "translation units (%0 vs. %1)">;
def err_unsupported_ast_node: Error<"cannot import unsupported AST node %0">;
}
