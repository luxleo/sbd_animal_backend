from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

# Create your models here.


def positive_validator(val):
    if val < 0:
        raise ValidationError("total calorie should be positive number")


def body_weight_validator(val):
    if val > 300 or val < 0:
        raise ValidationError("body weight should be positive number and less than 300")


class WorkoutType(models.Model):
    name = models.CharField(max_length=30)
    workout_distance = models.DecimalField(
        max_digits=3, decimal_places=2, validators=[positive_validator]
    )
    # TODO: add field 'target_muscles', 'sbd_related_percentage'
    category = models.CharField(max_length=3, blank=True)


class Log(models.Model):
    athlete = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    workout_type = models.ForeignKey(WorkoutType, on_delete=models.CASCADE)
    max_1rm = models.DecimalField(
        max_digits=5, decimal_places=1, validators=[positive_validator]
    )
    # TODO: max_power = models.PositiveSmallIntegerField(blank=True)
    total_cal = models.DecimalField(
        max_digits=5, decimal_places=1, validators=[positive_validator]
    )
    total_lift = models.DecimalField(
        max_digits=5, decimal_places=1, validators=[positive_validator]
    )
    created_at = models.DateField(auto_now_add=True)
    # 체중별 랭크 측정 위해 필요한 필드
    body_weight = models.DecimalField(
        max_digits=4, decimal_places=1, validators=[body_weight_validator]
    )
    percentile = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        validators=[positive_validator],
        blank=True,
        null=True,
    )
    num_sets = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["-id", "-created_at"]


class Rep(models.Model):
    log = models.ForeignKey(Log, on_delete=models.CASCADE)
    rep_order_number = models.PositiveSmallIntegerField()
    # TODO: avg_power = models.PositiveSmallIntegerField(blank=True)
    calorie = models.DecimalField(
        max_digits=5, decimal_places=1, validators=[positive_validator]
    )
    workout_weight = models.DecimalField(
        max_digits=5, decimal_places=1, validators=[positive_validator]
    )
    # 운동한 횟수 reps
    reps = models.PositiveSmallIntegerField()

    @property
    def one_rap_max(self):
        """
        using O’Conner formula
        :return:
        """
        if self.reps == 1:
            return self.workout_weight
        else:
            from decimal import Decimal

            res = int(float(self.workout_weight) * (1 + (0.025 * float(self.reps))))
            return res

    @property
    def lift_weight(self):
        return self.workout_weight * self.reps

    def __str__(self):
        return f"세트: {self.rep_order_number} 운동무게: {self.workout_weight} 반복횟수: {self.reps} 칼로리:{self.calorie} 1RM: {self.one_rap_max}  "

    class Meta:
        ordering = ["-id", "rep_order_number"]


class WorkoutRangePreference(models.Model):
    athlete = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    workout_type = models.ForeignKey(WorkoutType, on_delete=models.CASCADE)
    custom_range = models.DecimalField(
        max_digits=5, decimal_places=2, validators=[positive_validator]
    )
