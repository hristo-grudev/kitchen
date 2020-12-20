from django.db import models


class Recipes(models.Model):
    name = models.CharField("recipe name", max_length=200, )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Products(models.Model):
    name = models.CharField('product name', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Main(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    qty = models.CharField(max_length=25)

    def __str__(self):
        return str(self.recipe)


class Order(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    order_id = models.IntegerField()
    order_name = models.TextField(max_length=400)

    def __str__(self):
        return self.recipe

    class Meta:
        ordering = ('recipe', )