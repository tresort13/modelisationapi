from django.db import models

# Create your models here.
class PopulationProvince(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)
    

class TauxNataliteMortalite(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)
    
    
class TauxCroissanceProvince(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)
    
    
class ReellePopulationProvince(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)
    
    
class TauxMigrationProvince(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)
    
class PopulationTotalProvinceApresMigration(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)
    
class PopulationActiveOffreEmploi(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)
    
class PopulationActiveOffreEmploiSecteur(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)
    
class DonneeConsommation(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)
    
class DonneeInvestissementPrive(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)
    
class DonneeDepenseCourante(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)
    
class DonneeDepenseCapitale(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)
    
class DonneeDepensePublique(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)
    
class DonneeExportation(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)
    
class DonneeImportation(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)
    
    
class ExportationNettesPays(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)    
    
class CalculeDemandeInterieure(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)    
    
class CalculeProductionDomestique(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True) 
    
class DonneeProduction(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)  
    
class ImpotDGI(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)
    
class ImpoExpoDGDA(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)
    
class RecettesDGDA(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)
    
class RecettesDGRAD(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)

class RevenusSalaires(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)
    
class ExedantBrutExploitation(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)

class AutresImpots(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)
    
class SubventionProduction(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)

class SubventionConsommation(models.Model):
    fichier = models.FileField(upload_to='files')
    date_heure_envoie =models.DateTimeField(auto_now_add=True)
    date_envoie = models.DateField(auto_now_add=True)
    
    