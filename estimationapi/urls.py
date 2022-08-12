from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views
from knox import views as knox_views
from .views import LoginAPI
from .views import RegisterAPI

urlpatterns = [
    path('',views.welcom, name='welcom'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/population/',views.population,name='population'),
    path('api/tauxNataliteMortalite/',views.tauxNataliteMortalite,name='tauxNataliteMortalite'),
    path('api/tauxCroissance/',views.tauxCroissance, name='tauxCroissance'),
    path('api/tailleReellePopulation/',views.tailleReellePopulation, name='tailleReellePopulation'),
    path('api/tauxMigrationProvince/',views.tauxMigrationProvince, name='tauxMigrationProvince'),
    path('api/tauxMigration/',views.tauxMigration, name='tauxMigration'),
    path('api/populationActiveOffre/',views.populationActiveOffre, name='populationActiveOffre'),
    path('api/populationActiveOffreSecteur/',views.populationActiveOffreSecteur, name='populationActiveOffreSecteur'),
    path('api/donneeConsommation/',views.donneeConsommation, name='donneeConsommation'),
    path('api/donneeInvestissementPrive/',views.donneeInvestissementPrive, name='donneeInvestissementPrive'),
    path('api/donneeDepenseCourante/',views.donneeDepenseCourante, name='donneeDepenseCourante'),
    path('api/donneeDepenseCapital/',views.donneeDepenseCapital, name='donneeDepenseCapital'),
    path('api/depenseCourante/',views.depenseCourante, name='depenseCourante'),
    path('api/depenseCapital/',views.depenseCapital, name='depenseCapital'),
    path('api/donneeExportation/',views.donneeExportation, name='donneeExportation'),
    path('api/donneeImportation/',views.donneeImportation, name='donneeImportation'),
    path('api/donneeImportationAuto/',views.donneeImportationAuto, name='donneeImportationAuto'),
    path('api/donneeExportationAuto/',views.donneeExportationAuto, name='donneeExportationAuto'),
    path('api/donneeConsommationAuto/',views.donneeConsommationAuto, name='donneeConsommationAuto'),
    path('api/donneeInvestissementPriveAuto/',views.donneeInvestissementPriveAuto, name='donneeInvestissementPriveAuto'),
    path('api/donneeProduction/',views.donneeProduction,name='donneeProduction')
]

urlpatterns = format_suffix_patterns(urlpatterns)
