from warehouse.field import Field
from warehouse.model import Model
from warehouse.model_manager import ModelManager


class APIModelManager(ModelManager):
    def get_team_model(self) -> Model:
        fields = [
            Field(crawler_name='Nombre corto', target_name='nombreAbreviado'),
            Field(crawler_name='Nombre completo', target_name='nombreCompleto'),
            Field(crawler_name='Nombre del equipo', target_name='nombre'),
            Field(crawler_name='Entrenador'),
            Field(crawler_name='Presidente', target_name='presidente'),
            Field(crawler_name='URL del equipo en RF', target_name='url'),
            Field(crawler_name='Año de Fundación', target_name='fundacion', datatype='int'),
            Field(crawler_name='Sitio Web', target_name='web'),
            Field(crawler_name='Ciudad', target_name='ciudad'),
            Field(crawler_name='País', target_name='pais'),
            Field(crawler_name='Socios', datatype='int'),
            Field(crawler_name='Patrocinador'),
            Field(crawler_name='Marca de Ropa'),
        ]

        to_str = lambda f: f"{f.get_value_for('Nombre completo')} [{f.get_value_for('Nombre corto')}]"

        return Model(fields=fields, key_matches_manager='Nombre del equipo', key_string=to_str)

    def get_stadium_model(self) -> Model:
        fields = [
            Field(crawler_name='Nombre', target_name='nombre'),
            Field(crawler_name='Capacidad', target_name='capacidad', datatype='int'),
            Field(crawler_name='Dirección'),
            Field(crawler_name='Localidad', target_name='ciudad'),
            Field(crawler_name='Tamaño', target_name='dimensiones'),
            Field(crawler_name='Fecha construcción', datatype='int', target_name='construccion'),
            Field(crawler_name='País', target_name='pais'),
            Field(crawler_name='Equipo')
        ]

        return Model(fields=fields, key_matches_manager='Nombre')

    def get_player_model(self) -> Model:
        fields = [
            Field(crawler_name='Nombre', target_name='apodo'),
            Field(crawler_name='Completo', target_name='nombre'),
            Field(crawler_name='Fecha de nacimiento', target_name='fechaNacimiento'),
            Field(crawler_name='Lugar de nacimiento', target_name='paisNacimiento'),
            Field(crawler_name='País', target_name='nacionalidad'),
            Field(crawler_name='Altura', datatype='int'),
            Field(crawler_name='Peso', datatype='int'),
            Field(crawler_name='Demarcación', target_name='posicion'),
            Field(crawler_name='Equipo'),
            Field(crawler_name='Dorsal', datatype='int')
        ]

        return Model(fields=fields, key_matches_manager='')
