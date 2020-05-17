"""empty message

Revision ID: 80766d0ceee6
Revises: 
Create Date: 2020-05-10 20:20:57.991118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80766d0ceee6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Artist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('genres', sa.PickleType(), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('website', sa.String(length=120), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.Column('seeking_venue', sa.Boolean(), nullable=True),
    sa.Column('seek_description', sa.String(length=300), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.Column('past_shows', sa.PickleType(), nullable=True),
    sa.Column('upcoming_shows', sa.PickleType(), nullable=True),
    sa.Column('past_shows_count', sa.Integer(), nullable=True),
    sa.Column('upcoming_shows_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Venue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('genres', sa.PickleType(), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('website', sa.String(length=120), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.Column('seeking_talent', sa.Boolean(), nullable=True),
    sa.Column('seek_description', sa.String(length=120), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.Column('past_shows', sa.PickleType(), nullable=True),
    sa.Column('upcoming_shows', sa.PickleType(), nullable=True),
    sa.Column('past_shows_count', sa.Integer(), nullable=True),
    sa.Column('upcoming_shows_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('artist_image_link', sa.String(length=300), nullable=True),
    sa.Column('artist_name', sa.String(length=120), nullable=True),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('venue_name', sa.String(length=120), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('start_time', sa.String(length=120), nullable=False),
    sa.Column('end_time', sa.String(length=120), nullable=False),
    sa.Column('show_fee', sa.String(length=120), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Show')
    op.drop_table('Venue')
    op.drop_table('Artist')
    # ### end Alembic commands ###
