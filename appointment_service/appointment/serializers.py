from rest_framework import serializers

class AppointmentSerializer(serializers.Serializer):
    id         = serializers.CharField(read_only=True)
    patient_id = serializers.IntegerField()
    doctor_id  = serializers.IntegerField()
    date       = serializers.DateTimeField()

    def create(self, validated_data):
        from .models import Appointment
        # Tạo và lưu document trong MongoDB
        return Appointment(**validated_data).save()

    def to_representation(self, instance):
        """Chuyển document thành dict JSON"""
        return {
            'id': str(instance.id),
            'patient_id': instance.patient_id,
            'doctor_id': instance.doctor_id,
            'date': instance.date.isoformat(),
        }
