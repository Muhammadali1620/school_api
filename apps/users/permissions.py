from rest_framework import permissions


class AddTeacherPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('users.add_teachers')
    

class ViewTeacherPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('users.view_teachers')


class DeleteTeacherPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('users.delete_teachers')


class ChangeTeacherPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('users.change_teachers')
    

class AddStudentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('users.add_students')


class ViewStudentPermission(permissions.BasePermission):
        def has_permission(self, request, view):
            return request.user.has_perm('users.view_students')
        

class DeleteStudentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('users.delete_students')


class ChangeStudentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('users.change_students')
    

class AddAttendancePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('attendances.add_attendance')
    

class AddSubjectPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('subjects.add_subjects')
    

class AddStudentGroupPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('student_groups.add_studentgroups')
    

class ViewStudentGroupPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('student_groups.view_studentgroups')