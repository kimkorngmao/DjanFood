from django.db import models

# Create your models here.

class Food(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    category = models.CharField(max_length=150, null=True)
    special_price = models.IntegerField(null=True, blank=True)
    is_premium = models.BooleanField(default=False)
    promotion_end_at = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    image_relative_url = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return "{} (id: {})".format(self.title, self.id)
    
    class Meta:
        ordering = ['-created_at']
    
class Cart(models.Model):
    user = models.ForeignKey(to="auth.User", on_delete=models.CASCADE, related_name="food_cart")
    food = models.ForeignKey(to=Food, on_delete=models.CASCADE, related_name="cart")
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} x {self.food.title}"
    
    def total_price(self):
        price_to_use = self.food.special_price if self.food.special_price is not None else self.food.price
        return self.quantity * price_to_use
    
    class Meta:
        ordering = ['-created_at']