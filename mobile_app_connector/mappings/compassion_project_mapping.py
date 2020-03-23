# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2018 Compassion CH (http://www.compassion.ch)
#    @author: Quentin Gigon <gigon.quentin@gmail.com>
#
#    The licence is in the file __manifest__.py
#
##############################################################################

from odoo.addons.message_center_compassion.mappings.base_mapping import \
    OnrampMapping


class MobileLocationMapping(OnrampMapping):
    ODOO_MODEL = 'compassion.project'
    MAPPING_NAME = 'mobile_app_project'

    CONNECT_MAPPING = {
        'Latitude': 'gps_latitude',
        'Longitude': 'gps_longitude',
    }

    FIELDS_TO_SUBMIT = {k: None for k, v in CONNECT_MAPPING.iteritems() if v}


class MobileProjectMapping(OnrampMapping):
    ODOO_MODEL = 'compassion.project'
    MAPPING_NAME = 'mobile_app_project'

    CONNECT_MAPPING = {
        'AddressStreet': 'street',
        'AirportDistance': 'closest_airport_distance',
        'AirportPreferredTransportation': 'transport_mode_to_airport',
        'AirportTravelTime': 'time_to_airport',
        'AllocatedSurvivalSlots': None,
        'AnnualPrimarySchoolCostLocalCurrency': 'annual_primary_school_cost',
        'AnnualSecondarySchoolCostLocalCurrency':
            'annual_secondary_school_cost',
        'AvailableForVisits': 'available_for_visits',
        'AverageCoolestTemperature': 'average_coolest_temperature',
        'AverageWarmestTemperature': 'average_warmest_temperature',
        'ChildDevelopmentCenterName': 'child_center_original_name',
        'ChildDevelopmentCenterNameLocalLanguage': (
            'preferred_lang_id.name', 'res.lang.compassion'),
        'ChurchMinistry': ('ministry_ids.name', 'fcp.church.ministry'),
        'City': 'city',
        'Climate': 'community_climate',
        'ClosestMajorCityEnglish': 'closest_city',
        'Cluster': 'cluster',
        'CognitiveActivities0To5': ('cognitive_activity_babies_ids.name',
                                    'fcp.cognitive.activity'),
        'CognitiveActivities12Plus': ('cognitive_activity_ados_ids.name',
                                      'fcp.cognitive.activity'),
        'CognitiveActivities6To11': ('cognitive_activity_kids_ids.name',
                                     'fcp.cognitive.activity'),
        'CommunityInvolvement': None,
        'Community_Name': 'community_name',
        'CompassionConnectEnabled': None,
        'ComputersForBeneficiaryUse': 'nb_child_computers',
        'ComputersForStaffUse': 'nb_staff_computers',
        'CoolestMonth': 'coolest_month',
        'Country': ('country_id.name', 'res.country'),
        'CountryDivision': 'state_province',
        'Country_Name': None,
        'CulturalRitualsAndCustoms': 'cultural_rituals',
        'CurrentStageInQavahProcess': None,
        'Denomination': 'church_denomination',
        'EconomicNeedDescription': 'economic_needs',
        'EducationalNeedDescription': 'education_needs',
        'ElectricalPowerAvailability': 'electrical_power',
        'Facilities': ('facility_ids.name', 'fcp.church.facility'),
        'FacilityOwnershipStatus': 'church_ownership',
        'FamilyMonthlyIncome': 'monthly_income',
        'FieldOffice_Country': ('field_office_id.country',
                                'compassion.field.office'),
        'FieldOffice_Name': ('field_office_id.name',
                             'compassion.field.office'),
        'FieldOffice_RegionName': ('field_office_id.region',
                                   'compassion.field.office'),
        'FirstLetterWritingMonth': 'first_scheduled_letter',
        'FirstPartnershipAgreementSignedDate': None,
        'FloorArea': None,
        'FoundationDate': 'church_foundation_date',
        'GPSLatitude': 'gps_latitude',
        'GPSLongitude': 'gps_longitude',
        'HarvestMonths': ('harvest_month_ids.name', 'connect.month'),
        'HealthContextNeeds': 'health_needs',
        'HomeBasedSponsorshipBeneficiaries': None,
        'HomeFloor': 'typical_floor_material',
        'HomeRoof': 'typical_roof_material',
        'HomeWall': 'typical_wall_material',
        'HungerMonths': ('hunger_month_ids.name', 'connect.month'),
        'ICPStatus': 'status',
        'ICP_ID': 'fcp_id',
        'ICP_Name': 'local_church_name',
        'ICP_NameNonLatin': 'local_church_original_name',
        'ImplementedProgram': ('implemented_program_ids.name', 'fcp.program'),
        'InterestedGlobalPartnerName': ('interested_partner_ids.name',
                                        'compassion.global.partner'),
        'InternationalDenominationAffiliation': 'international_affiliation',
        'InternetAccess': 'church_internet_access',
        'IsParticipatingInQavahProcess': None,
        'LastReviewedDate': 'last_reviewed_date',
        'LocaleType': 'community_locale',
        'MajorRevision_RevisedValues': None,
        'MobileInternetAccess': ('mobile_device_ids.value',
                                 'fcp.mobile.device'),
        'MonthSchoolYearBegins': 'school_year_begins',
        'NumberOfActiveMembers': 'number_church_members',
        'NumberOfClassrooms': 'nb_classrooms',
        'NumberOfLatrines': 'nb_latrines',
        'NumberOfSponsorshipBeneficiaries': 'nb_cdsp_kids',
        'NumberOfSurvivalBeneficiaries': None,
        'OnSiteInternetQuality': None,
        'PhysicalActivities0To5': ('physical_activity_babies_ids.name',
                                   'fcp.physical.activity'),
        'PhysicalActivities12Plus': ('physical_activity_ados_ids.name',
                                     'fcp.physical.activity'),
        'PhysicalActivities6To11': ('physical_activity_kids_ids.name',
                                    'fcp.physical.activity'),
        'PlantingMonths': ('planting_month_ids.name', 'connect.month'),
        'Population': 'community_population',
        'PostalCode': 'zip_code',
        'PreferredLanguage': ('preferred_lang_id.name', 'res.lang.compassion'),
        'PrimaryDiet': ('primary_diet_ids.name', 'fcp.diet'),
        'PrimaryEthnicGroup': 'primary_ethnic_group_name',
        'PrimaryLanguage': ('primary_language_id.name', 'res.lang.compassion'),
        'PrimaryOccupation': ('primary_adults_occupation_ids.value',
                              'fcp.community.occupation'),
        'ProgramBreakReason': None,
        'ProgramBreakStartDate': None,
        'ProgramEndDate': 'program_end_date',
        'ProgramStartDate': 'program_start_date',
        'ProgramsOfInterest': ('interested_program_ids.name', 'fcp.program'),
        'ProjectActivitiesForFamilies': None,  #
        'RainyMonths': ('rainy_month_ids.name', 'connect.month'),
        'SchoolCostPaidByICP': ('school_cost_paid_ids.value',
                                'fcp.school.cost'),
        'SecondLetterWritingMonth': 'second_scheduled_letter',
        'SocialMedia': 'social_media_site',
        'SocialNeedsDescription': 'social_needs',
        'SocioEmotionalActivities0To5': ('socio_activity_babies_ids.value',
                                         'fcp.sociological.activity'),
        'SocioEmotionalActivities12Plus': ('socio_activity_ados_ids.value',
                                           'fcp.sociological.activity'),
        'SocioEmotionalActivities6To11': ('socio_activity_kids_ids.value',
                                          'fcp.sociological.activity'),
        'SourceKitName': None,

        'SpiritualActivities0To5': ('spiritual_activity_babies_ids.value',
                                    'fcp.spiritual.activity'),
        'SpiritualActivities12Plus': ('spiritual_activity_ados_ids.value',
                                      'fcp.spiritual.activity'),
        'SpiritualActivities6To11': ('spiritual_activity_kids_ids.value',
                                     'fcp.spiritual.activity'),
        'Terrain': 'community_terrain',
        'Territory': 'territory',
        'TranslationCompletedFields': None,
        'TranslationRequiredFields': None,
        'TranslationStatus': None,
        'TravelTimeToMedicalServices': 'time_to_medical_facility',
        'UnemploymentRate': 'unemployment_rate',
        'UtilitiesOnSite': ('utility_ids.name', 'fcp.church.utility'),
        'WarmestMonth': 'warmest_month',
        'Website': 'website',
        'WeeklyChildAttendance': 'weekly_child_attendance',
        'icpbio': None,
        'icpbioInHtml': None
    }

    FIELDS_TO_SUBMIT = {k: None for k, v in CONNECT_MAPPING.iteritems() if v}

    def _process_connect_data(self, connect_data):
        for key, value in connect_data.copy().iteritems():
            if not value:
                del connect_data[key]
        return connect_data