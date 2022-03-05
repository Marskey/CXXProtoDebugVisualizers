import lldb

def Protobuf_RepeatedField_Summary(valobj,internal_dict,options):
	ret = ""
	if valobj.TypeIsPointerType():
		ret = hex(valobj.GetValueAsUnsigned()) + " "
	return ret + "size=" + str(valobj.GetNumChildren())

class Protobuf_RepeatedField:
	def __init__(self, valobj, internal_dict):
		self.valobj = valobj
		self.count = None

	def num_children(self):
		if self.count is None:
			self.count = self.num_children_impl()
		return self.count

	def num_children_impl(self):
		try:
			return self.valobj.GetChildMemberWithName('current_size_').GetValueAsUnsigned()
		except:
			return 0

	def get_child_index(self, name):
		try:
			return int(name.lstrip('[').rstrip(']'))
		except:
			return -1

	def get_child_at_index(self, index):
		if index < 0: return None
		if index > self.num_children(): return None
		try:
			offset = index * self.data_size
			return self.arena.CreateChildAtOffset('[' + str(index) + ']', offset, self.data_type)
		except:
			return None

	def extract_type(self):
		list_type = self.valobj.GetType().GetUnqualifiedType()
		if list_type.IsPointerType():
			list_type = list_type.GetPointeeType()
		elif list_type.IsReferenceType():
			list_type = list_type.GetDereferencedType()

		if list_type.GetNumberOfTemplateArguments() > 0:
			data_type = list_type.GetTemplateArgumentType(0)
		else:
			data_type = None
		return data_type

	def update(self):
		self.count = None
		try:
			self.data_type = self.extract_type()
			self.data_size = self.data_type.GetByteSize()
			self.arena = self.valobj.GetChildMemberWithName('arena_or_elements_')
			if self.arena.IsValid() and self.valobj.GetChildMemberWithName('current_size_').IsValid():
				self.count = None
			else:
				self.count = 0

		except Exception as e:
			print(str(e))
			self.count = 0
		return False

class Protobuf_RepeatedPtrField:
	def __init__(self, valobj, internal_dict):
		self.valobj = valobj
		self.count = None

	def num_children(self):
		if self.count is None:
			self.count = self.num_children_impl()
		return self.count

	def num_children_impl(self):
		try:
			return self.valobj.GetChildMemberWithName('current_size_').GetValueAsUnsigned()
		except:
			return 0

	def get_child_index(self, name):
		try:
			return int(name.lstrip('[').rstrip(']'))
		except:
			return -1

	def get_child_at_index(self, index):
		if index < 0: return None
		if index > self.num_children(): return None
		try:
			offset = index * self.data_size
			return self.rep.GetChildMemberWithName('elements').CreateChildAtOffset('[' + str(index) + ']', offset, self.data_type)
		except:
			return None

	def extract_type(self):
		list_type = self.valobj.GetType().GetUnqualifiedType()
		if list_type.IsPointerType():
			list_type = list_type.GetPointeeType()
		elif list_type.IsReferenceType():
			list_type = list_type.GetDereferencedType()

		if list_type.GetNumberOfTemplateArguments() > 0:
			data_type = list_type.GetTemplateArgumentType(0).GetPointerType()
		else:
			data_type = None
		return data_type


	def update(self):
		self.count = None
		try:
			self.data_type = self.extract_type()
			self.data_size = self.data_type.GetByteSize()
			self.rep = self.valobj.GetChildMemberWithName('rep_')
			if self.rep.IsValid() and self.valobj.GetChildMemberWithName('current_size_').IsValid():
				self.count = None
			else:
				self.count = 0

		except Exception as e:
			print(str(e))
			self.count = 0
			pass

