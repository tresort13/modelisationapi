from rest_framework import serializers

from .models import CalculeDemandeInterieure, CalculeProductionDomestique, DonneeConsommation, DonneeDepenseCapitale, DonneeDepenseCourante, DonneeDepensePublique, DonneeExportation, DonneeImportation, DonneeInvestissementPrive, DonneeProduction, ExportationNettesPays, PopulationActiveOffreEmploi, PopulationActiveOffreEmploiSecteur, PopulationProvince, PopulationTotalProvinceApresMigration, ReellePopulationProvince, TauxCroissanceProvince, TauxMigrationProvince, TauxNataliteMortalite,ImpotDGI,ImpoExpoDGDA
from django.contrib.auth.models import User


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class PopulationProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopulationProvince
        fields = ['id', 'fichier']
        
class TauxNataliteMortaliteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TauxNataliteMortalite
        fields = ['id', 'fichier']
        
class TauxCroissanceProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TauxCroissanceProvince
        fields = ['id', 'fichier']
        
class ReellePopulationProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReellePopulationProvince
        fields = ['id', 'fichier']
        
class TauxMigrationProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TauxMigrationProvince
        fields = ['id', 'fichier']
        
class PopulationTotalProvinceApresMigrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopulationTotalProvinceApresMigration
        fields = ['id', 'fichier']
        
class PopulationActiveOffreEmploiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopulationActiveOffreEmploi
        fields = ['id', 'fichier']

class PopulationActiveOffreEmploiSecteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopulationActiveOffreEmploiSecteur
        fields = ['id', 'fichier']
        
class DonneeConsommationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonneeConsommation
        fields = ['id', 'fichier']
        
class DonneeInvestissementPriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonneeInvestissementPrive
        fields = ['id', 'fichier']
        
class DonneeDepenseCouranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonneeDepenseCourante
        fields =  ['id', 'fichier']
        
class DonneeDepenseCapitaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonneeDepenseCapitale
        fields =  ['id', 'fichier']
        
class DonneeDepensePubliqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonneeDepensePublique
        fields = ['id', 'fichier']
        
class DonneeExportationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonneeExportation
        fields =  ['id', 'fichier']
        
class DonneeImportationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonneeImportation
        fields =  ['id', 'fichier']
        
class ExportationNettesPaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExportationNettesPays
        fields = ['id', 'fichier']
        
class CalculeDemandeInterieureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculeDemandeInterieure
        fields = ['id', 'fichier']
        
class CalculeProductionDomestiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculeProductionDomestique
        fields = ['id', 'fichier']
        
        
class DonneeProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonneeProduction
        fields =  ['id', 'fichier']
        
class ImpotDGISerializer(serializers.ModelSerializer):
    class Meta:
        model = ImpotDGI
        fields =  ['id', 'fichier']
        
class ImpoExpoDGDASerializer(serializers.ModelSerializer):
    class Meta:
        model = ImpoExpoDGDA
        fields =  ['id', 'fichier','taux_exportation','taux_importation']
        
        
        
        
        
