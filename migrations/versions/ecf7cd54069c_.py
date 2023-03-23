"""empty message

Revision ID: ecf7cd54069c
Revises: 2525c2699a12
Create Date: 2023-03-20 19:03:39.360343

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ecf7cd54069c'
down_revision = '2525c2699a12'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cleaning',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('adresse', sa.String(length=64), nullable=True),
    sa.Column('wohnung', sa.String(length=64), nullable=True),
    sa.Column('status', sa.String(length=64), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('bemerkunng', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('cleaning', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_cleaning_adresse'), ['adresse'], unique=False)
        batch_op.create_index(batch_op.f('ix_cleaning_bemerkunng'), ['bemerkunng'], unique=False)
        batch_op.create_index(batch_op.f('ix_cleaning_date'), ['date'], unique=False)
        batch_op.create_index(batch_op.f('ix_cleaning_name'), ['name'], unique=False)
        batch_op.create_index(batch_op.f('ix_cleaning_status'), ['status'], unique=False)
        batch_op.create_index(batch_op.f('ix_cleaning_wohnung'), ['wohnung'], unique=False)

    with op.batch_alter_table('schedule', schema=None) as batch_op:
        batch_op.drop_index('ix_schedule_adresse')
        batch_op.drop_index('ix_schedule_appartment')
        batch_op.drop_index('ix_schedule_date')
        batch_op.drop_index('ix_schedule_notes')
        batch_op.drop_index('ix_schedule_status')

    op.drop_table('schedule')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schedule',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('adresse', mysql.VARCHAR(collation='utf8mb3_bin', length=255), nullable=True),
    sa.Column('appartment', mysql.VARCHAR(collation='utf8mb3_bin', length=64), nullable=True),
    sa.Column('date', mysql.DATETIME(), nullable=True),
    sa.Column('status', mysql.VARCHAR(collation='utf8mb3_bin', length=64), nullable=True),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('notes', mysql.VARCHAR(collation='utf8mb3_bin', length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='schedule_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb3_bin',
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('schedule', schema=None) as batch_op:
        batch_op.create_index('ix_schedule_status', ['status'], unique=False)
        batch_op.create_index('ix_schedule_notes', ['notes'], unique=False)
        batch_op.create_index('ix_schedule_date', ['date'], unique=False)
        batch_op.create_index('ix_schedule_appartment', ['appartment'], unique=False)
        batch_op.create_index('ix_schedule_adresse', ['adresse'], unique=False)

    with op.batch_alter_table('cleaning', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_cleaning_wohnung'))
        batch_op.drop_index(batch_op.f('ix_cleaning_status'))
        batch_op.drop_index(batch_op.f('ix_cleaning_name'))
        batch_op.drop_index(batch_op.f('ix_cleaning_date'))
        batch_op.drop_index(batch_op.f('ix_cleaning_bemerkunng'))
        batch_op.drop_index(batch_op.f('ix_cleaning_adresse'))

    op.drop_table('cleaning')
    # ### end Alembic commands ###
