"""init

Revision ID: 5ba7d439bba3
Revises: 
Create Date: 2025-05-20 22:09:48.186530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ba7d439bba3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('country', sa.String(length=2), nullable=False),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('aqi_snapshots',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=False),
    sa.Column('pm25', sa.Float(), nullable=True),
    sa.Column('pm10', sa.Float(), nullable=True),
    sa.Column('aqi', sa.Integer(), nullable=True),
    sa.Column('pollutant', sa.String(length=10), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['cities.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('aqi_snapshots')
    op.drop_table('cities')
    # ### end Alembic commands ###
