from django.contrib import admin
from .models import Discount, OrderDetail, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem    
    fields = ['quantity', 'final_price']

class OrdersAdmin(admin.ModelAdmin):
    list_display = ['pk', 'get_name', 'get_total', 'created_at', 'status']
    # ordering = ['-created']
    list_filter = ['status', 'created_at']
    search_fields = ['user__username']
    search_help_text = 'Поиск по имени/фамилии'
    readonly_fields = ['created']
    
    def get_name(self, obj):
        return obj.user.username
      
    get_name.admin_order_field = 'client-name'
    get_name.short_description = 'Имя клиента'
    
    
    readonly_fields = ['created_at']    
    inlines = [
        OrderItemInline,
    ]
    


admin.site.register(Discount)
admin.site.register(OrderDetail, OrdersAdmin)
# admin.site.register(OrderItem)
