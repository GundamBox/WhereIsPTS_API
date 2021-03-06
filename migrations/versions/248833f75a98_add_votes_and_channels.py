"""add votes and channels

Revision ID: 248833f75a98
Revises: 6b95156e615a
Create Date: 2019-04-23 16:17:29.059534

"""
import geoalchemy2
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '248833f75a98'
down_revision = '6b95156e615a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('channel',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=128), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.execute("INSERT INTO channel(name) VALUES ('公視新聞'),('TVBS新聞'),('中天新聞'),('民視新聞'),('中視新聞'),('華視新聞'),('三立新聞'),('東森新聞'),('年代新聞'),('非凡新聞'),('壹電視新聞'),('體育新聞'),('不是新聞');")

    op.create_table('vote',
                    sa.Column('sid', sa.Integer(), nullable=False),
                    sa.Column('cid', sa.Integer(), nullable=False),
                    sa.Column('vote_count', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['cid'], ['channel.id'], ),
                    sa.ForeignKeyConstraint(['sid'], ['store.id'], ),
                    sa.PrimaryKeyConstraint('sid', 'cid')
                    )
    op.add_column('store', sa.Column(
        'disable_vote', sa.Integer(), nullable=False))
    op.add_column('store', sa.Column('enable', sa.Boolean(), nullable=False))
    op.add_column('store', sa.Column('geom', geoalchemy2.types.Geometry(
        geometry_type='POINT'), nullable=False))
    op.add_column('store', sa.Column(
        'last_ip', sa.String(length=40), nullable=False))
    op.add_column('store', sa.Column(
        'last_modified', sa.DateTime(), nullable=False))
    op.drop_column('store', 'lng')
    op.drop_column('store', 'lastModified')
    op.drop_column('store', 'lat')
    op.drop_column('store', 'news')
    op.drop_column('store', 'ip')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('store', sa.Column('ip', sa.VARCHAR(
        length=40), autoincrement=False, nullable=False))
    op.add_column('store', sa.Column('news', sa.VARCHAR(
        length=128), autoincrement=False, nullable=False))
    op.add_column('store', sa.Column('lat', postgresql.DOUBLE_PRECISION(
        precision=53), autoincrement=False, nullable=False))
    op.add_column('store', sa.Column('lastModified',
                                     postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.add_column('store', sa.Column('lng', postgresql.DOUBLE_PRECISION(
        precision=53), autoincrement=False, nullable=False))
    op.drop_column('store', 'last_modified')
    op.drop_column('store', 'last_ip')
    op.drop_column('store', 'geom')
    op.drop_column('store', 'enable')
    op.drop_column('store', 'disable_vote')

    op.drop_table('vote')
    op.drop_table('channel')
    # ### end Alembic commands ###
